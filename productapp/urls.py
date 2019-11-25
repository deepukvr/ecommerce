from django.urls import path
from productapp import views
app_name='productapp'

urlpatterns=[
    path('search',views.search),
]