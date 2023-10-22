from django.shortcuts import render
from .models import Product
from .forms import SearchForm
from django.core.paginator import Paginator,EmptyPage
# Create your views here.

def index(request):
   
    products=Product.objects.all()
    
    search_form=request.GET.get("item name")
    if search_form != None :
        products=Product.objects.filter(title__icontains=search_form)
    p=Paginator(products,4)   
    return render(request,"shop/index.html",{
        "items":products,
        
    })

