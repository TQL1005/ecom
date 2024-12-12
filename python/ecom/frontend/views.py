from django.shortcuts import render
import requests
# Create your views here.

def index(request):   
    return render(request,'index.html')


def store(request):
    r = requests.get('http://127.0.0.1:8000/api/product')
    products = []
    for x in r.json():
        products.append({
            'name': x['name'],
            'id':x['id'],
            'price': x['price'],
            'images': x['images']
        })
    context = {'products': products}
    return render(request,'store.html',context=context)

def cart(request):
    r = requests.get('http://127.0.0.1:8000/api/order_item')
    order_item = []
    total = 0 
    for x in r.json():
        order_item.append({
            'id': x['id'],
            'product': x['product'],    
            'quantity': x['quantity'],
        })
        total = total + x['quantity']
    context = {'order_item': order_item,'total':total}
    return render(request,'cart.html',context=context)
    