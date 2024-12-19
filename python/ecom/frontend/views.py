from django.shortcuts import render
import requests
# Create your views here.

def index(request):   
    r = requests.get('http://127.0.0.1:8000/api/order_item')
    response_data = r.json()
    total = response_data['total_quantity']
    if (total == None):
        total = 0
    context = {'total':total}
    return render(request,'index.html',context=context)

def data_store(request):
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
    return context


def data_cart(request):
    r = requests.get('http://127.0.0.1:8000/api/order_item')
    order_item = []
    response_data = r.json()
    items = response_data['items'] 
    total = response_data['total_quantity']
    total_price =  response_data['total_price'] 
    product_orderitem =  response_data['product_orderitem'][0][1]
    if (total == None):
        total = 0
    if (total_price == None):
        total_price = 0
    for x in items:
        order_item.append({
            'id': x['id'],
            'product': x['product'],    
            'quantity': x['quantity'],
        })
    context = {'order_item': order_item,'total':total,'total_price':total_price,'product_orderitem':product_orderitem}
    return context

def store(request):
    context = data_store(request)
    return render(request,'store.html',context=context)

def cart(request):
    context = data_cart(request)
    return render(request,'cart.html',context=context)

def checkout(request):
    context = data_cart(request)
    return render(request,"checkout.html",context=context)
    