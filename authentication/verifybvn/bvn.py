from config import settings
import requests

class Bvn():
    def verify(bvn):
        baseUrl = settings.FLUTTER_WAVE_URL

        headers = {
        'Content-Type': 'application/json',
        'Authorization':'Bearer '+ settings.FLUTTER_WAVE_SECRET_KEY
        }
        
        response = requests.get(url = baseUrl+"/kyc/bvns/"+bvn, headers=headers)
        return response
