********** ****Services**** **********

1)***Registering a drone***
URL = http://127.0.0.1:8000/manage-drone (POST)
BODY (JSON) =  {
            "serialNumber": "AAA_3000_ABC_VS-0.1",     
            "model": "Lightweight",
            "weightLimit": 100,
            "battery": 25,
            "state": "IDLE",
            "medicationLoad": [                                     ###-Medication IDs
                2
            ]
        } 
RETURN  =  (JSON {"data":new Drone})
           "data": {
                "id": 7,
                "serialNumber": "AAA_3000_ABC_VS-0.1",
                "model": "Lightweight",
                "weightLimit": 100,
                "battery": 25,
                "state": "IDLE",                                     
                "medicationLoad": [                               
                    2
                ]
    }

2)***loading a drone with medication items***
URL = http://127.0.0.1:8000/load-drone (PUT)
BODY (JSON) =    {
			"droneId":"7" ,                                         ### this service first find the drone by the id if this field does not exist then use the serial number 
			"droneSerialNumber":"AAA_3000_ABC_VS-0.",               ###
            "medicationLoad": [2]                                   ### Medication IDs
            
        }
RETURN = (JSON {"data":Drone update})
        "data": {
            "id": 7,
            "serialNumber": "AAA_3000_ABC_VS-0.2",
            "model": "Lightweight",
            "weightLimit": 200,
            "battery": 25,
            "state": "LOADED",                                      ### the state change to LOADED
            "medicationLoad": [                                     ### the new medications are add to the drone
                2
            ]
    }

3)***checking loaded medication items for a given drone***
URL = http://127.0.0.1:8000/check-drone-load (GET)
BODY (JSON) =    {
			"droneId":"7" ,                                         ### this service first find the drone by the id if this field does not exist then use the serial number 
			"droneSerialNumber":"AAA_3000_ABC_VS-0.",               ###
        }
RETURN = (JSON {"data":[Medications]})
        "data": [
                {
                    "id": 2,
                    "name": "Dipyrone",
                    "weight": 100,
                    "code": "L2023_V2025",
                    "image": "/Dipyrone.jpg"
                }
            ]

4)***checking available drones for loading***
URL = http://127.0.0.1:8000/check-idle-drones (GET)
RETURN = (JSON {"data":[Drones]})
      "datos": [
        {
            "id": 7,
            "serialNumber": "AAA_3000_ABC_VS-0.2",
            "model": "Lightweight",
            "weightLimit": 200,
            "battery": 25,
            "state": "LOADED",                                     
            "medicationLoad": [                                  
                2
            ]
        },
        {
            "id": 7,
            "serialNumber": "AAA_3000_ABC_VS-0.3",
            "model": "Lightweight",
            "weightLimit": 100,
            "battery": 55,
            "state": "IDLE",                                     
            "medicationLoad": [                                  
            ]
        }
    ]

5)***check drone battery level for a given drone***
URL = http://127.0.0.1:8000/check-drone-batrery (GET)
BODY (JSON) =    {
			"droneId":"7" ,                                         ### this service first find the drone by the id if this field does not exist then use the serial number 
			"droneSerialNumber":"AAA_3000_ABC_VS-0.",               ###
        }
RETURN = (JSON {"data": battery})
        "data": [
                {
                    "battery": 25
                }
            ]