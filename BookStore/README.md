Requirements :
Django
Pillow 		(Using to work with ImageField)
psycopg2 	(Using to work with postgresql database)
zeep		(Using to work with online payment services)
django-allauth	(Using to make User registration)


Perform the following operations before running the project:
- Use pgAdmin4 to make a database named "shopdb"
-Inter the information of your database in setting file(DATABASES section)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shopdb',
        'USER': 'postgres',
        'PASSWORD': '******',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

-Follow this link instructions to make Google Developer Console :
https://console.developers.google.com/

-Set Email Information in Setting File (needed to send confirmation Email):
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'Your Email'
EMAIL_HOST_PASSWORD = 'Your Email Password'

-Enter Your merchant code In shop\views.py file for connecting to Online Payament Services 
(In This Project we Use ZarinPal services)
 
