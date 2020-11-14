import requests
import time
import logging
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w', format="%(levelname)s %(asctime)s %(message)s")

URL = os.getenv('SERVER')
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
FROM_NUMBER = os.getenv('FROM_NUMBER')
TO_NUMBER = os.getenv('TO_NUMBER')
MESSAGE_TEXT = f'Server is down {URL}'

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def sms_send():
        message = client.messages.create(
            body=MESSAGE_TEXT + str(response.ok),
            from_=FROM_NUMBER,
            to=TO_NUMBER,
            )
        logging.info(f'Message succesfully sent. SID: {message.sid}')
       
response = requests.get(URL)
while response.ok:
    logging.info('Checking server')
    time.sleep(60)
else:
    logging.warning('Server is down, sending sms')
    sms_send()
    
        
    