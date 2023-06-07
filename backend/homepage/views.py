from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .serializers import MessageSerializer, EmailSerializer
from .models import Messages, EmailIds
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def homepage(request):
    return HttpResponse("Hello world")
    
@api_view(['GET', 'POST'])
def message_view(request):
    if request.method == 'GET':
        queryset = Messages.objects.all()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)
    
@csrf_exempt
@api_view(['GET', 'POST'])
def message_post(request):
    if request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message = "Data saved successfully"
            return Response({'message': message}, status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['GET', 'POST'])
def fetch_all_emails(request):
    if request.method == 'GET':
        queryset = EmailIds.objects.all()
        serializer = EmailSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
@csrf_exempt
@api_view(['GET', 'POST'])
def post_email(request):
    if(request.method == 'POST'):
        serializer=EmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message="Data saved successfully"
            return Response({"message":message}, status=201)
        return Response(serializer.errors, status=400)