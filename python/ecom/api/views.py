from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .supabase_client import supabase


@api_view(['GET','POST'])
def Customer(request):
    if request.method == 'GET':
        response = supabase.table("Customer").select("*").execute()
        return Response(response.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        customer_data = request.data
        response = supabase.table("Customer").insert(customer_data).execute()
        return Response(response.data,status=status.HTTP_201_CREATED)


@api_view(['GET','POST'])
def Product(request):
    if request.method == 'GET':
        response = supabase.table("Product").select("*").execute()
        return Response(response.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        customer_data = request.data
        response = supabase.table("Product").insert(customer_data).execute()
        return Response(response.data,status=status.HTTP_201_CREATED)

