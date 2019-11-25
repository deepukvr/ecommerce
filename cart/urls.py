
from django.urls import path
from cart import views
app_name='cart'

urlpatterns=[
    path('addcart/',views.addcart,name='addcart'),
path('insertcart/', views.insertcart, name='insertcart'),
path('cart/',views.cart, name='cart'),
    path('deletecart/',views.deletecart, name='deletecart'),
    path('modifycart/', views.modifycart, name='modifycart'),
    path('modifiedcart/', views.modifiedcart, name='modifiedcart'),
]