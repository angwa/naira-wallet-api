import requests
from config import settings

class SendSMS():
    def send():
        url = settings.TERMII_SMS_URL
        payload  = {
            "to": "+2347062423707",
            "from": "Techrald",
            "sms": "Hi there, testing Termii",
            "type": "plain",
            "channel": "Whatsapp",
            "api_key": settings.TERMI_SMS_SECRET_KEY,
        }

        headers = {
        'Content-Type': 'application/json',
        }

        response = requests.post(url = url, headers = headers, json=payload)

        return response
