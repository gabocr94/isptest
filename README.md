# Isptest
Test for django rest framework and local IVR calls.

Description
----
A rest service for an internet service provider (ISP). This service will feed a website where users can register, make and check payments, get information such as own profile, internet plans and speeds, payment dates, change plans and ubsubscribe from the service.

Also the service feeds a IVR where users are able to make payments, check next payment date and amount or get information about plans and speeds.

Solution
-----
First, using django rest framework:
	
	Register and login will use Django authentication.
	The models will be Customer, Plan, Contract and Payment.
	DRF permissions and decorators to add security on the application.
	Use stripe to manage payments.
	Using POST code to send data to the service, and GET to retrieve data from it.
	Admins will use django admin site to manage plans and prices.
	
Using Asterisk/Pystrix:

	User needs to type in id card, the system will reply with a welcome [name] message, or an 		error message when the user is not registered into the application.
	
	After checking in the id card, the system will reply with a few options:
		
	Make payment: Users will type in the credit card, cvc, and expiration date.
	Check user plan and speed.
	Ask for next payment date.
	
	Hang up.
	