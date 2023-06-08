from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .helper import proccessUrl, setLoad, checkLoad, IdleDrones, getDroneBattery, getDroneBatteryLogs

# Create your views here.
@csrf_exempt
def SeeElements(request, idAux=0):
    return proccessUrl(request, idAux)


@csrf_exempt
def loadDrone(request, idAux=0):
    return setLoad(request, idAux)

@csrf_exempt
def checkLoadDrone(request, idAux=0):
    return checkLoad(request)

@csrf_exempt
def checkIdleDrones(request, idAux=0):
    return IdleDrones(request)


def checkDroneBattery(request, idAux=0):
    return getDroneBattery(request, idAux=0)

def checkDroneBatteryLogs(request, idAux=0):
    return getDroneBatteryLogs(request)