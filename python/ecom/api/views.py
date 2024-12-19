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
    
@api_view(['GET','POST'])
def Order_item(request):
    if request.method == 'GET':
        response = supabase.table("OrderItem").select("*").execute()

        # Sum the quantity field
        response2 = supabase.rpc("sum_quantity").execute()
        #Sum the price*quantity
        response3 = supabase.rpc("sum_money").execute()

        response4 = supabase.rpc("join_product_orderitem").execute()
        # Extract the total quantity from the response
        total_quantity = response2.data

        # Extract the total quantity from the response
        total_price = response3.data
        # Combine data and total quantity in the response
        product_orderitem = response4
        data = {
            "items": response.data,
            "total_quantity": total_quantity,
            "total_price": total_price,
            'product_orderitem':product_orderitem
        }

        return Response(data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        customer_data = request.data
        response = supabase.table("OrderItem").insert(customer_data).execute()
        return Response(response.data,status=status.HTTP_201_CREATED)
    
@api_view(['POST'])
def Order_item_update (request):
    if request.method == 'POST':
        customer_data = request.data
        productId = customer_data[0]['product']
        print(int(productId))
        try:
            response = supabase.rpc("update_quantity2", {"product_id": int(productId)}).execute()
            return Response(response.data, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            print("Error:", e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def process_order(request):
    if request.method == 'POST':
        shipping_address = request.data['shipping']
        print(shipping_address)
        response = supabase.table("ShippingAddress").insert(shipping_address).execute()
        if response:
            return Response(response.data, status=status.HTTP_200_OK)

        
