from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!'})

@api_view(['GET'])
def get_question(request):
    currentQuestion = request.param.currentQuestion 
    
    return Response({'message': 'Hello, world!'})