from django.shortcuts import render
from prize_draw.models import PrizeDraw
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from awards.models import Awards

# Create your views here.
#global variables
content_type ='application/json; charset=UTF-8'
status_202 =status.HTTP_202_ACCEPTED
status_400 = status.HTTP_400_BAD_REQUEST
status_401 = status.HTTP_401_UNAUTHORIZED
status_404 = status.HTTP_404_NOT_FOUND

@api_view(['POST'])
def CreateAwards(request):
    
    if not request.data.get('prize_number'):
        return Response({"message":"Número do premio não informado."},status=status_400, content_type=content_type)
    else:
        #passar pela urls
        object_prize_draw = PrizeDraw.objects.get(id=1)
        obj = Awards()
        obj.prize_draw_id = object_prize_draw
        obj.prize_number = request.data['prize_number']
        obj.description_prize = request.data['description_prize']
        obj.save()
    return Response({"message": "Premio cadastrado"})
        