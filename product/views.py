from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
# def index(request):
#    return HttpResponse("Product page here")


def index(request):
    # product =
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
