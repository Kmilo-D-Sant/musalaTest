********** Services **********

1)-Registering a drone
URL = http://127.0.0.1:8000/manage-drone (POST)
BODY (JSON) =  {
            "serialNumber": "AAA_3000_ABC_VS-0.1",
            "model": "Lightweight",
            "weightLimit": 234,
            "battery": 25,
            "state": "IDLE",
            "medicationLoad": [
                2
            ]
        } 