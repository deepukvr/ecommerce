from django.shortcuts import render
from .models import Product
def search(request):
    x=request.GET['pcat']
    y=request.GET["pname"]
    recs=Product.objects.filter(pcat=x,pname=y)
    return render(request,"product.html",{'recs':recs})


