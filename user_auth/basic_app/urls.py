from .views import *
from django.urls import path

app_name = "basic_app"
urlpatterns = [
            path('', index, name='index'),
            path('login', user_login, name='user_login'),
            path('signup', signup, name='signup'),
]