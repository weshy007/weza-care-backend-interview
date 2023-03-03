from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name="login"),
    path('activate/<uidb64>/<token>/', views.ActivateAccount.as_view(), name='activate'),

]
