from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from prize_draw.models import PrizeDraw
from oauth2_provider.models import AccessToken
# Create your views here.

#global variables
content_type ='application/json; charset=UTF-8'
status_202 =status.HTTP_202_ACCEPTED
status_400 = status.HTTP_400_BAD_REQUEST
status_401 = status.HTTP_401_UNAUTHORIZED
status_404 = status.HTTP_404_NOT_FOUND

#criação do sorteio
@api_view(['POST'])
def CreatePrizeDraw(request):
    if request.auth == None:
        return Response({"message": "Não logado!"}, status=status_401, content_type=content_type)
    
    #acesso com o token da autenticação
    access_token = AccessToken.objects.get(token=request.auth) 
    if access_token:
        if not request.data.get('name'):
            return Response({"message":"Número do premio não informado."},status=status_400, content_type=content_type)
        else:
            obj = PrizeDraw()
            obj.user_id = access_token.user.pk
            obj.name = request.data['name']
            obj.descricao = request.data['descricao']
            obj.price = request.data['price']
            obj.qtd_prize_draw = request.data['qtd_prize_draw']
            obj.date_prize_draw = request.data['date_prize_draw']
            obj.status = request.data['status']
            obj.save()
        return Response({"message": "Sorteio cadastrado"})