from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Forged
from .serializers import ForgedSerializer




@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_forged(request, pk):
    try:
        forged = Forged.objects.get(pk = pk)
    except Forged.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)  

    if request.method == 'GET':
        serializer = ForgedSerializer(forged)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        return Response({})          
    elif request.method == 'PUT':
        return Response({})


@api_view(['GET', 'POST'])
def get_post_forged(request):
    if request.method == 'GET':
        forged = Forged.objects.all()
        serializer = ForgedSerializer(forged, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'length': int(request.data.get('length')),
            'blade': request.data.get('blade'),
            'steelgrade': request.data.get('steelgrade')
        } 
        serializer = ForgedSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)    
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)            