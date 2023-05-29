from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from oauthlib.common import generate_token
from oauth2_provider.models import AccessToken, Application
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
# Create your views here.
#global variables
content_type ='application/json; charset=UTF-8'
status_202 =status.HTTP_202_ACCEPTED
status_400 = status.HTTP_400_BAD_REQUEST
status_401 = status.HTTP_401_UNAUTHORIZED
status_404 = status.HTTP_404_NOT_FOUND
User = get_user_model()

#cadastro de usuario
@api_view(['POST'])
def Register(request):
    password_user = request.data['password'] 
    email = request.data['email']
    username = request.data['name']
    user = User.objects.create_user(username, email, password_user)
    return Response({"message": str(user)}, content_type=content_type)
    
#Login do usuario
@api_view(['POST'])
def Login(request):
    password_user = request.data['password'] 
    email = request.data['email']
    getUser =  User.objects.get(email=email)
    tok = generate_token()
    app = Application.objects.first()
    user = User.objects.filter(email=email).first()
    
    if not request.data.get('email') or not request.data.get('password'):
        return Response({"message": "Email ou senha não informado!"},status=status_400, content_type=content_type)
    
    #função internar interna do django - check_password -
    elif check_password(password=password_user, encoded=getUser.password):  
        access_token = AccessToken.objects.create(user=user, application=app, expires=timezone.now() + relativedelta(days=1), token=tok)
        return Response({"message": str(access_token)}, content_type=content_type)
    else:
        return Response({"message": "Senha errada"}, content_type=content_type)
    