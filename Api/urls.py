from django.urls import path
from .admin import MODELS_DICTIONARY
from . import views

app_name = 'Api'


def createPaths():
    diccionario = {}
    diccionario['load-drone'] = views.loadDrone
    diccionario['check-drone-load'] = views.checkLoadDrone
    diccionario['check-idle-drones'] = views.checkIdleDrones
    diccionario['check-drone-batrery'] = views.checkDroneBattery
    diccionario['check-drone-batrery-logs'] = views.checkDroneBatteryLogs
    

    return diccionario


PATHS_DICTIONARY = createPaths()

urlpatterns = []
urlpatterns += map(lambda key: path(key[0], key[1]), PATHS_DICTIONARY.items())
urlpatterns += map(lambda key: path(key[0] +
                   '/', key[1]), PATHS_DICTIONARY.items())

urlpatterns += map(lambda key: path(key, views.SeeElements),
                   MODELS_DICTIONARY.keys())
urlpatterns += map(lambda key: path(key+'/', views.SeeElements),
                   MODELS_DICTIONARY.keys())
urlpatterns += map(lambda key: path(key+'/<str:idAux>',
                   views.SeeElements), MODELS_DICTIONARY.keys())