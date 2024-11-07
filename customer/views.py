from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import (TokenObtainPairView)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from .serializers import LoginSerializer
from payment.models import Payment
from payment.paystack import Paystack
import requests
from django.conf import settings

# Create your views here.
class LoginView(ViewSet):

    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            return InvalidToken(e)
        except Exception as e:
            return Response({"message":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class UserAsetsView(ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, req):
        return Response({"message":"Finishing"})
    

# class VerifyPayment(APIView):
#     def get(self, req):
#         ref = req.get('ref')
#         payment = Payment.objects.get(ref=ref)
#         verified = payment.verify_payment()

#         if verified:
#             last_order = 


class PayStackTransactionInitializationView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):
        url = "https://api.paystack.co/transaction/initialize"
        email = request.data.get('email')
        amount = request.data.get('amount')

        # print(f'{email} {amount}')
        # return
    
        if not email or not amount:
            return Response({"error":"Email and amount are required"}, status=status.HTTP_400_BAD_REQUEST)
    

        data = {
                "email":email,
                "amount": amount
            }
        
        headers = {

            'Authorization': f'Bearer {settings.PAYSTACK_PRIVATE_KEY}',
            'Cache-control': 'no-cache'
        }

        reponse = requests.post(url,headers=headers, data=data)

        if reponse.status_code == 200:
            return Response(reponse.json(), status=status.HTTP_200_OK)
        else:
            return Response(reponse.json(), status=status.HTTP_400_BAD_REQUEST)
    
            