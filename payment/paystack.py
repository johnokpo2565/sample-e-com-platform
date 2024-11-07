from django.conf import settings
import secrets
import requests

class Paystack:
    PAYSTACK_SK = settings.PAYSTACK_PRIVATE_KEY
    # PAYSTACK_PK = settings.PAYSTACK_PUBLIC_KEY
    base_url = 'https//api.paystack.co/'

    def verifypayment(self, ref, *args, **kwargs):
        path = f'transaction/verify/{ref}'
        headers = {
           'Authorization': f'Bearer {self.PAYSTACK_SK}',
           'Content_Type':'application/json',  
        }

        url = self.base_url + path
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            response.data = response.json()
            return response.data['status'], response.data['data']
        
        response.data = response.json()
        return response.data['status'], response.data['message']