from Api.admin import MODELS_DICTIONARY
from Api.const import *
from inspect import Parameter
from rest_framework import serializers, status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .models import *


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
            object = model.objects.get(id=id)
            serializer = modelSerializer(object, data=data)
            if serializer.is_valid(raise_exception=True):
                object = serializer.save()
                return answer(serializer.data, status.HTTP_202_ACCEPTED)

        if request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = modelSerializer(data=data)
            droneAux = Drone(data)
            weight = droneAux.__calculateWeight__()
            droneAux.weight = weight
            isValid = Drone(data).__validate__()   
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


def answer(datos, estado=status.HTTP_200_OK):
    return JsonResponse({"datos": datos}, status=estado)


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
    if request.method == 'POST':
        return answer("pepe")
    return error(MESSAGE_DATA_DOES_NOT_MEET_REQUIREMENTS, status.HTTP_406_NOT_ACCEPTABLE)

def proccessUrl(request, idAux):
    try:
        model = getModelByUrl(request)
        return manageElements(request, model, idAux)
    except BaseException as err:
        return handleError(err)


#verificar que la suma del peso este bien