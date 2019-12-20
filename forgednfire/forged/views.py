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
        return Response({})
    elif request.method == 'DELETE':
        return Response({})          
    elif request.method == 'PUT':
        return Response({})


@api_view(['GET', 'POST'])
def get_post_forges(request):
    if requested.method == 'GET':
        return Response({})
    elif requested.method == 'POST': 
        return Response({})            