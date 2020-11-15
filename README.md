## About the Project
Script checking site accessability every 60 seconds. If server is down user will know about it via SMS. 

## Installation
1. Register at [Twilio](https://www.twilio.com) and add own Twilio account sid and Auth token values to .env file, located in the same directory with the program.
2. Add virtual phone number obtained in Twilio and phone number you want to receive sms to .env file
3. Install all required libraries(requests,time,logging,os,dotenv,Client from twillio.rest). You can do it by using command "pip install *library name*
4. Add site you want to check to .env file and start the program. 
