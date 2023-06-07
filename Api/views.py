from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .helper import proccessUrl

# Create your views here.
@csrf_exempt
def SeeElements(request, idAux=0):
    return proccessUrl(request, idAux)

