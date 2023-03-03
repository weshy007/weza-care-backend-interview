from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.models import auth
from django.views import View

from .models import CustomUser
from .utils import account_activation_token


# Create your views here.
@transaction.atomic
def signup(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('signup')
            elif CustomUser.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return redirect('signup')
            else:
                user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                      email=email, password=password)

                current_site = get_current_site(request)
                mail_subject = "Account Activation"
                message = render_to_string("activation/activate.html", {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": account_activation_token.make_token(user)
                })

                email_message = EmailMessage(
                    mail_subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [email]
                )

                email_message.send()

                return render(request, "activation/message.html")
        else:
            messages.info(request, "Passwords must match")
            return redirect("signup")
    return render(request, "account/signup.html")


def login_user(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('users')

    else:
        return render(request, "account/login.html")


class ActivateAccount(View):
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()

            messages.success(request, {"Your account has been approved"})
            return redirect("login")

        else:
            messages.warning(request, "The confirmation link was invalid or has been already used")
            return redirect("signup")