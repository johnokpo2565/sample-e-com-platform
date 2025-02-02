from django.db import models
import secrets
from .paystack import Paystack

# Create your models here.

class Payment(models.Model):
    amount = models.IntegerField(blank=True, null=True)
    ref = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.amount}'
    

    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)

            object_with_similar_ref = Payment.objects.filter(ref=ref)

            if not object_with_similar_ref:
                self.ref = ref
            super().save(*args, **kwargs)

    

    def amount_value(self):
        return int(self.amount) * 100
    

    def verify_payment(self):
        paystack = Paystack()
        status, result = paystack.verifypayment(self.ref, self.amount)

        if status :
            if result['amount'] / 100 == self.amount :
                self.verified = True
                self.save()
            
        if self.verified:
            return True
        else:
            return False
