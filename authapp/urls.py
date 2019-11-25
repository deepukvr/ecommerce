from authapp import views
from authapp.views import login
from django.conf.urls import url
from . import views
from django.urls import path
app_name='authapp'
urlpatterns=[
#url(r'^signin/$',views.signin),
url(r'^signup/$',views.signup),
path('login/',views.login),
path('my_logout/',views.my_logout),
#path('search',views.search),
url(r'^signup/otpvalidation$',views.otpvalidation),



]
