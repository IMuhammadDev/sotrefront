from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q , F
from store.models import Produckt , OrderItem , Order , Customer

# Create your views here.

def say_hello(request):
    
    quer_set = Order.objects.select_related('customer').prefetch_related('items').order_by('-placed_at')[:5]

    return render(request , 'hello.html' , {'name':'mosh', "orders": list(quer_set) })

