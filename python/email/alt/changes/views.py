from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

def members(request):
    return render(request,"alt/index.html")

