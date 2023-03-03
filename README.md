## Weza Care Internship Challenge

## Get Started
### Clone Project:
```
$ git clone git clone https://github.com/weshy007/weza-care-backend-interview.git 
$ cd weza-care-backend-interview
```
### Migrate database:
The database being used is PostgreSQL. Create it and put it in the `.env` file

    $ python manage.py makemigrations
    $ python manage.py migrate

### Technologies Used
- Python - Django Framework
    - Djoser - Authentication with token
- Rest Framework

### BDD
- Users can create an account as well as log in to the platform
- Users can post questions on the platform
- Users can answer questions posted only by others on the platform
- Given an ID, users can retrieve a particular question with that ID, along with the answers to
the question.
- User can view all the questions that they have ever asked on the platform

