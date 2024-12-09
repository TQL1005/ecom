from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Member
import json
from .serializer import Serializer


@api_view(['GET'])
def getAPI(request):
    member = Member.objects.all()
    serializer = Serializer(member, many=True)
    return Response(serializer.data) 

@api_view(['POST','GET'])
def postAPI(request):
    if request.method == 'POST':
        html_json_data = request.data.get('htmlJson')
        serializer = Serializer(data=request.data)
        if html_json_data:
            data = json.loads(html_json_data)
            if serializer.is_valid():
                for attr in data:
                    Member.objects.create(name=attr['name'], value=attr['value'])
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
    
    
    elif request.method == 'GET':
        member = Member.objects.all()
        serializer = Serializer(member, many=True)
        return Response(serializer.data)
    
@api_view(['PUT','GET'])
def putAPI(request,pk):
    if request.method == 'GET':
        member = Member.objects.get(pk=pk)
        serializer = Serializer(member)
        return Response(serializer.data)
    elif request.method == 'PUT':
        member = Member.objects.get(pk=pk)
        serializer = serializer(member)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delAPI(request,pk):
    member = Member.objects.get(pk=pk)
    member.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
