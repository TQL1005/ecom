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

def login(request):
    return render(request,'login.html')
