from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.apps import apps
from .models import Drone, Medication

admin.site.register(Drone)
admin.site.register(Medication)


def createDictionary():
    modelsDictionary = {}
    app_models = apps.get_app_config('Api').get_models()
    for model in app_models:
        route = "manage-" + model.__name__.lower()
        modelsDictionary[route] = model
    return modelsDictionary


MODELS_DICTIONARY = createDictionary()


def createDictionaryAttributes():
    app_models = apps.get_app_config('Api').get_models()

    attributeDictionary = {}
    for model in app_models:
        fieldList = []
        fields = model.objects.model._meta.get_fields(include_hidden=True)
        for field in fields:
            field = str(field)
            try:
                auxField = field[field.index(model.__name__+"."):]
                auxField = auxField[auxField.index(".")+1:]
            except:
                auxField = field[field.index(".")+1: -1]
            fieldList.append(auxField)
        attributeDictionary[model] = fieldList
    return attributeDictionary


ATTRIBUTE_DICTIONARY = createDictionaryAttributes()
