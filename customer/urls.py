from rest_framework.routers import SimpleRouter
from .views import LoginView,UserAsetsView, PayStackTransactionInitializationView

route = SimpleRouter()
route.register('auth/login', LoginView, basename='login')
route.register('assets', UserAsetsView, basename='assets')
# route.register('payment/initialize', PayStackTransactionInitializationView, basename='initializepayment')


urlpatterns = route.urls