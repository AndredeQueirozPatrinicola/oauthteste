from django.contrib import admin
from django.urls import path
from django_oauth_usp.accounts.views import accounts_authorize, accounts_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', accounts_login, name='login'),
    path('authorize', accounts_authorize, name='authorize'),
]

