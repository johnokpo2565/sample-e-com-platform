from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.


class VerifyPayment(APIView):
    def get(self, req, ref):
        pass
