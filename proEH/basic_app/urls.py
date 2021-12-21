from django.conf.urls import url
from django.urls import path
from basic_app import views

# Template URL's!
app_name = 'basic_app'

urlpatterns= [
    path('register/',views.register,name='register'),
    path('userlogin/',views.user_login,name='user_login'),
]
