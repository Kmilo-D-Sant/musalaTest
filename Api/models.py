from django.db import models

from django.db import models
import re
from django.http.response import JsonResponse
from rest_framework import status
    
MODELS = (("Lightweight", "Lightweight"), ("Middleweight", "Middleweight"), ("Cruiserweight", "Cruiserweight"),
    ("Heavyweight", "Heavyweight"))
STATE =  (("IDLE", "IDLE"), ("LOADING", "LOADING"), ("LOADED", "LOADED"),
    ("DELIVERING", "DELIVERING"), ("DELIVERED", "DELIVERED"), ("RETURNING", "RETURNING"))


class Medication(models.Model):
    

    name = models.CharField("Name", max_length=50, blank=False, null=False)
    weight = models.FloatField("Weight")
    code = models.CharField("Code", max_length=100, blank=False, null=False)
    image = models.ImageField("Image", blank=False, null=False)

    def validate(self):
        exLetterNumberScriptUndersocre = "^[0-9a-zA-Z_-]*$"
        exLetterUpNumberUnderscore = "^[0-9A-Z_]*$"
        if re.match(exLetterNumberScriptUndersocre, self.pk["name"]) == None:
            return  JsonResponse({"error":"The name allowed only letters, numbers, '-' and '_'"}, status=status.HTTP_400_BAD_REQUEST)
        if re.match(exLetterUpNumberUnderscore, self.pk["code"]) == None:
            return  JsonResponse({"error":"The code allowed only upper case letters, underscore and numbers"}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({"data": "Data is OK"}, status=status.HTTP_200_OK)

class Drone(models.Model):
    
    serialNumber = models.CharField("Serial number", max_length=100, blank=False, null=False)
    model = models.CharField("Model", max_length=50, choices=MODELS)
    medicationLoad = models.ManyToManyField(Medication, null=True, blank=True)
    weight = models.FloatField("Weigh limit", blank=True, null=True)
    battery = models.IntegerField("Battery", blank=False, null=False)
    state = models.CharField("State", max_length=50, choices=STATE)
    
    
    
    def __calculateWeight__(self):
        medicationsIds = self.pk["medicationLoad"]
        weight = 0
        for id in medicationsIds:
            weight += Medication.objects.get(id=id).weight
        self.pk["weight"] = weight
        return weight
     
    def __validate__(self):
        exLen = "^(.){1,100}$"
        
        if re.match(exLen, self.pk["serialNumber"]) == None:
            return JsonResponse({"error":"The name only permits 100 characters max"}, status=status.HTTP_400_BAD_REQUEST)
        if self.pk["weightLimit"] > 500:
            return JsonResponse({"error":"The weight can't be bigger than 500gr"}, status=status.HTTP_400_BAD_REQUEST) 
        if self.pk["battery"] > 100 or self.pk["battery"] < 0:
            return JsonResponse({"error":"The battery percent can't be bigger than 100 or smaller than 0"}, status=status.HTTP_400_BAD_REQUEST)  
        if self.pk["model"] in ["Lightweight", "Middleweight", "Cruiserweight", "Heavyweight"] == False:
            return JsonResponse({"error":"Model most be one of the next four models: Lightweight, Middleweight, Cruiserweight and Heavyweight"}, status=status.HTTP_400_BAD_REQUEST)  
        if self.pk["state"] in ["IDLE", "LOADING", "LOADED", "DELIVERING", "DELIVERED", "RETURNING"] ==False:
            return JsonResponse({"error":"State most be one of the next six models: IDLE, LOADING, LOADED, DELIVERING, DELIVERED and RETURNING"}, status=status.HTTP_400_BAD_REQUEST) 

