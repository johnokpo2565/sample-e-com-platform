from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extrafeilds):
        
        if email is None:
            raise ValueError('Email is required')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extrafeilds)
        user.set_password(password)
        user.save(using=self._db)
    
    
    def create_superuser(self, email, password=None, **extrafeilds):
        extrafeilds.setdefault("is_staff",True)
        extrafeilds.setdefault("is_superuser", True)
        
        return self.create_user(email=email, password=password, **extrafeilds)
            