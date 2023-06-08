from Api.admin import MODELS_DICTIONARY
from Api.const import *
from inspect import Parameter
from rest_framework import serializers, status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
import threading
import datetime
import logging
import time

logging.basicConfig(filename='BatteryHistory.log', encoding='utf-8', level=logging.DEBUG)


def getModelByUrl(request):
    urlAux = request.META["PATH_INFO"][1:]
    try:
        url = urlAux[: urlAux.index("/")]
    except:
        url = urlAux
    return MODELS_DICTIONARY[url]


def proccessUrl(request, idAux):
    try:
        model = getModelByUrl(request)
        return manageElements(request, model, idAux)
    except BaseException as err:
        return handleError(err)


def strToInt(text: str):
    try:
        if text == None or text == "":
            return 0
        i = int(text)
        return i
    except:
        return -1


def generateSerializer(objectModel, obejectDepth=0):
    class serializerClass(serializers.ModelSerializer):
        class Meta:
            model = objectModel
            fields = '__all__'
            depth = obejectDepth

    return serializerClass


def answer(data, state=status.HTTP_200_OK):
    return JsonResponse({"data": data}, status=state)


def manageElements(request: Parameter, model: object, idAux: str):
    try:

        id = strToInt(idAux)
        if id < 0:
            return error(MESSAGE_INVALID_PARAMETER, status.HTTP_406_NOT_ACCEPTABLE)

        if request.method == 'GET':
            modelSerializer = generateSerializer(model)
            if id == 0:
                objetos = model.objects.all()
                data = modelSerializer(objetos, many=True).data
                return answer(data)
            else:
                object = model.objects.get(id=id)
                data = modelSerializer(object).data
                return answer(data)

        modelSerializer = generateSerializer(model)

        if request.method == 'PUT':
            data = JSONParser().parse(request)
            if id == 0:
                if data["id"] != None:
                    id = data["id"]
                    if not isNumber(data["id"]):
                        return error("The id most be a number", status.HTTP_406_NOT_ACCEPTABLE)
            isValid = model(data).__validate__()
            if isValid.status_code == status.HTTP_400_BAD_REQUEST:
                return isValid
            object = model.objects.get(id=id)
            serializer = modelSerializer(object, data=data)
            if serializer.is_valid(raise_exception=True):
                object = serializer.save()
                return answer(serializer.data, status.HTTP_202_ACCEPTED)

        if request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = modelSerializer(data=data)
            isValid = model(data).__validate__()
            if isValid.status_code == status.HTTP_400_BAD_REQUEST:
                return isValid
            if serializer.is_valid(raise_exception=True):
                if isValid.status_code == status.HTTP_200_OK:
                    object = serializer.save()
                    return answer(serializer.data, status.HTTP_201_CREATED)

        if request.method == 'DELETE':
            object = model.objects.get(id=id)
            serializer = modelSerializer(object)
            object.delete()
            return answer(serializer.data, status.HTTP_202_ACCEPTED)

        return error(MESSAGE_DATA_DOES_NOT_MEET_REQUIREMENTS, status.HTTP_406_NOT_ACCEPTABLE)

    except BaseException as err:
        return handleError(err)


def error(message: str, state=status.HTTP_400_BAD_REQUEST):
    return JsonResponse({"error": message}, status=state)


def answer(data, estado=status.HTTP_200_OK):
    return JsonResponse({"data": data}, status=estado)


def handleError(err):
    strTypeError = str(type(err))
    strError = str(err)
    msg = f"{strTypeError} {strError}"
    try:
        if strTypeError.__contains__(CHECK_DONT_EXIST):
            return error(MESSAGE_ELEMENT_NOT_EXIST, status.HTTP_404_NOT_FOUND)
        elif strTypeError.__contains__(CHECK_PARSE_ERROR):
            return error(MESSAGE_DATA_DOES_NOT_MEET_REQUIREMENTS, status.HTTP_406_NOT_ACCEPTABLE)
        elif strTypeError.__contains__(CHECK_KEY_ERROR):
            return error(f'{MESSAGE_INVALID_PARAMETER} ({strError})', status.HTTP_406_NOT_ACCEPTABLE)
        elif strTypeError.__contains__(CHECK_TYPE_ERROR):
            if strError.find(': ', 0) != -1:
                p = strError.index(': ')
                if p >= 0:
                    strError = strError[p+2:]
            return error(f'{MESSAGE_INVALID_PARAMETER} ({strError})', status.HTTP_406_NOT_ACCEPTABLE)
        elif strTypeError.__contains__(CHECK_VALIDATION_ERROR):
            return error(f'{MESSAGE_INVALID_PARAMETER} ({strError})', status.HTTP_406_NOT_ACCEPTABLE)
        return error(msg)
    except BaseException as newError:
        return error(f"{str(type(newError))} {str(newError)}")


def setLoad(request, idAux):
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        try:
            if data["droneId"] != None:
                if not isNumber(data["droneId"]):
                    return error("The id most be a number", status.HTTP_406_NOT_ACCEPTABLE)
                try:
                    object = Drone.objects.get(id=data["droneId"])
                except:
                    return error(f"There is not coincidences for this id({data['droneId']})", status.HTTP_406_NOT_ACCEPTABLE)
        except:
            try:
                if data["droneSerialNumber"] != None:
                    try:
                        object = Drone.objects.get(serialNumber=data["droneSerialNumber"])
                    except:
                        return error(f"There is not coincidences for this serial number({data['droneSerialNumber']})", status.HTTP_406_NOT_ACCEPTABLE)
            except:
                return error("Please provide the droneId or droneSerialNumber field", status.HTTP_406_NOT_ACCEPTABLE)

        try:
            if data["medicationLoad"] != None:
                dataAux = {
                    "serialNumber": object.serialNumber,
                    "model": object.model,
                    "weightLimit": object.weightLimit,
                    "battery": object.battery,
                    "state": "LOADING",
                    "medicationLoad": data["medicationLoad"]
                }
        except:
            return error("Please provide the medicationLoad field", status.HTTP_406_NOT_ACCEPTABLE)

        modelSerializer = generateSerializer(Drone)
        isValid = Drone(dataAux).__validate__()
        if isValid.status_code == status.HTTP_400_BAD_REQUEST:
            return isValid
        dataAux["state"] = "LOADED"
        serializer = modelSerializer(object, data=dataAux)
        if serializer.is_valid(raise_exception=True):
            object = serializer.save()
            return answer(serializer.data, status.HTTP_202_ACCEPTED)
    return error(MESSAGE_DATA_DOES_NOT_MEET_REQUIREMENTS, status.HTTP_406_NOT_ACCEPTABLE)


def checkLoad(request):
    if request.method == 'GET':
        data = JSONParser().parse(request)
        try:
            if data["droneId"] != None:
                if not isNumber(data["droneId"]):
                    return error("The id most be a number", status.HTTP_406_NOT_ACCEPTABLE)
                try:
                    object = Drone.objects.get(id=data["droneId"])
                except:
                    return error(f"There is not coincidences for this id({data['droneId']})", status.HTTP_406_NOT_ACCEPTABLE)
        except:
            try:
                if data["droneSerialNumber"] != None:
                    try:
                        object = Drone.objects.get(serialNumber=data["droneSerialNumber"])
                    except:
                        return error(f"There is not coincidences for this serial number({data['droneSerialNumber']})", status.HTTP_406_NOT_ACCEPTABLE)
            except:
                return error("Please provide the droneId or droneSerialNumber field", status.HTTP_406_NOT_ACCEPTABLE)
        modelSerializerDrone = generateSerializer(Drone)
        modelSerializerMedication = generateSerializer(Medication)
        medicationIdList = modelSerializerDrone(object).data["medicationLoad"]
        medicationList = Medication.objects.filter(id__in=medicationIdList)
        return answer(modelSerializerMedication(medicationList,  many=True).data)
    return error(MESSAGE_DATA_DOES_NOT_MEET_REQUIREMENTS, status.HTTP_406_NOT_ACCEPTABLE)


def IdleDrones(request):
    if request.method == 'GET':
        modelSerializer = generateSerializer(Drone)
        objetos = Drone.objects.filter(battery__gt=24, state="IDLE")
        data = modelSerializer(objetos, many=True).data
        return answer(data)
    return error(MESSAGE_DATA_DOES_NOT_MEET_REQUIREMENTS, status.HTTP_406_NOT_ACCEPTABLE)


def getDroneBattery(request, idAux=0):
    if request.method == 'GET':
        data = JSONParser().parse(request)
        try:
            if data["droneId"] != None:
                if not isNumber(data["droneId"]):
                    return error("The id most be a number", status.HTTP_406_NOT_ACCEPTABLE)
                try:
                    object = Drone.objects.get(id=data["droneId"])
                except:
                    return error(f"There is not coincidences for this id({data['droneId']})", status.HTTP_406_NOT_ACCEPTABLE)
        except:
            try:
                if data["droneSerialNumber"] != None:
                    try:
                        object = Drone.objects.get(serialNumber=data["droneSerialNumber"])
                    except:
                        return error(f"There is not coincidences for this serial number({data['droneSerialNumber']})", status.HTTP_406_NOT_ACCEPTABLE)
            except:
                return error("Please provide the droneId or droneSerialNumber field", status.HTTP_406_NOT_ACCEPTABLE)
        return answer({"battery": object.battery})
    return error(MESSAGE_DATA_DOES_NOT_MEET_REQUIREMENTS, status.HTTP_406_NOT_ACCEPTABLE)


def getDroneBatteryLogs(request):
    if request.method == 'GET':
        object = Drone.objects.all()
        dataAnswer = []
        for drone in object:
            dataAnswer.append({"droneId": drone.id, "serialNumber":drone.serialNumber, "battery":drone.battery, "date":str(datetime.datetime.now())})
        
        return answer(dataAnswer)
    return error(MESSAGE_DATA_DOES_NOT_MEET_REQUIREMENTS, status.HTTP_406_NOT_ACCEPTABLE)

def getDroneBatteryLogsTest():
    while True:
        object = Drone.objects.all()
        for drone in object:
            logging.info({"droneId": drone.id, "serialNumber":drone.serialNumber, "battery":drone.battery, "date":str(datetime.datetime.now())})
        time.sleep(600)
        

t = threading.Thread(target= getDroneBatteryLogsTest)
t.start()




def proccessUrl(request, idAux):
    try:
        model = getModelByUrl(request)
        return manageElements(request, model, idAux)
    except BaseException as err:
        return handleError(err)




def isNumber(id):
    exNum = "^[0-9]+$"
    if re.match(exNum, str(id)) == None:
        return False
    return True


# verificar que la suma del peso este bien
