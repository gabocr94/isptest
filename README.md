# Isptest
Test for django rest framework and local IVR calls.

Description
----
The application will set up a django rest service where users will be able to register,
and purchase an internet plan between a few options. It is a subscription based plan, so users will have to pay monthly.

When a user registers, and purchases a plan, the application creates a new contract for that customer,
with its personal information and the plan data.

Customers will be able to manage personal information, change plans, pay and unsubscribe from a website connected to the rest service.
Also an IVR call service will be set up for users to pay throughout their phones, check their next payment amount and date .



Solution
-----
First, using django framework:
	
	Register and login will use Django authentication.
	The models will be Customer, Plan, Contract and Payment.
	DRF permissions and decorators to add security on the application.
	Use stripe to manage payments.
	Using POST code to send data to the service, and GET to retrieve data from it.
	Admins will use django admin site to manage plans and prices.
	Mysql database to save models.
	Logging 
    The application will gather information from external forms and response in JSON objects.
	
Using Asterisk/Pystrix:

	User needs to type in id card, the system will reply with a welcome [name] message, or an 		error message when the user is not registered into the application.
	
	After checking in the id card, the system will reply with a few options:
		
	Make payment: Users will type in the credit card, cvc, and expiration date.
	Check user plan and speed.
	Ask for next payment date.
	
	Hang up.
	
Requirements
---
This applications uses mysql client, before running migrations run the following line
to prevent any fail.
    
        sudo apt-get install python-dev default-libmysqlclient-dev
        
Now you can run the requirements file into your virtual environment:
        
        pip install -r requirements.txt
 
Database
--

MySql 8.0 is the chosen database for this project. Before running initial migrations,
make sure that you change the database configuration in Settings.py file:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '[YOUR_SCHEMA]',
        'USER': '[YOUR_USER]',
        'PASSWORD': '[USER_PW]',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

       
Migrations
---

When you already set up your database and connection is working, you are ready to migrate models into your db.

    python manage.py migrate
    
Basic Configuration
---
Before running the application, create an admin user by running the following line:

    python manage.py createsuperuser