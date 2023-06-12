******************* *******Services******* *******************

*******RUN*******
("root")\musalaTest>python manage.py runserver

*******The function (getDroneBatteryLogsTest) check drone batteries levels every 10 minutes and save it in Battery History.log****

1)******Registering a drone******

URL = http://127.0.0.1:8000/manage-drone (POST)

BODY (JSON) =  
        {
            "serialNumber": <string with serial number of drone (1-100 characters max)>,     
            "model": <string with model, only one of this (Lightweight, Middleweight, Cruiserweight, Heavyweight)>,
            "weightLimit": <int with weight in gr (0-500gr max)>,
            "battery": <int represent the battery percentage (0-100)>
        } 

RETURN OK 
BODY (JSON) =     ### Example ###
        "data": 
        {
            "id": 7,
            "serialNumber": "AAA_3000_ABC_VS-0.1",
            "model": "Lightweight",
            "weightLimit": 100,
            "battery": 25,
            "state": "IDLE",                                     
            "medicationLoad": []
        }

RETURN FAILED 
BODY (JSON) = 
        {
            "error": "Especific error menssage "
        }



2)******loading a drone with medication items******

URL = http://127.0.0.1:8000/load-drone (PUT)

BODY (JSON) =    
        {
			"droneId":"Drone id (int, its needed at least one of bought fields(droneId or droneSerialNumber))" ,                                         r 
			"droneSerialNumber":"Drone serial number (string, its needed at least one of bought fields(droneId or droneSerialNumber))",               
            "medicationLoad": [
                {
                    "name": "string with medication name (allowed only letters, numbers, ‘-‘, ‘_’)",
                    "weight": int, with medication weight (0-infinite),
                    "code": "string with medication code (allowed only upper case letters, underscore and numbers)",
                    "image":"string with medication image (imagen encode with utf-8 in base64)"
                }
            ]                                 
        }

RETURN OK 
BODY (JSON) =     ### Example ###
        "data": 
        {
            "id": 7,
            "serialNumber": "AAA_3000_ABC_VS-0.2",
            "model": "Lightweight",
            "weightLimit": 200,
            "battery": 25,
            "state": "LOADED",                                      
            "medicationLoad": [                                    
                {
                    "id": 4,
                    "name": "Sedative",
                    "weight": 20,
                    "code": "VL2023_UNT2025",
                    "image": EXEMPLE_IMAGEN_IN_BASE64   ## variable at the end of the file
                }
            ]
        }

RETURN FAILED 
BODY (JSON) = 
        {
            "error": "Especific error menssage "
        }



3)******checking loaded medication items for a given drone******

URL = http://127.0.0.1:8000/check-drone-load (GET)

BODY (JSON) =    
        {
			"droneId":"Drone id (int, its needed at least one of bought fields(droneId or droneSerialNumber))" ,                                          
			"droneSerialNumber":"Drone serial number (string, its needed at least one of bought fields(droneId or droneSerialNumber))",               
        }

RETURN OK 
BODY (JSON) =     ### Example ###
        "data": 
            [
                {
                    "id": 2,
                    "name": "Dipyrone",
                    "weight": 100,
                    "code": "L2023_V2025",
                    "image": EXEMPLE_IMAGEN_IN_BASE64
                }
            ]

RETURN FAILED 
BODY (JSON) = 
        {
            "error": "Especific error menssage "
        }


4)******checking available drones for loading******

URL = http://127.0.0.1:8000/check-idle-drones (GET)      

RETURN OK 
BODY (JSON) =     ### Example ###
      "data": 
        [
            {
                "id": 7,                                                
                "serialNumber": "AAA_3000_ABC_VS-0.2",
                "model": "Lightweight",
                "weightLimit": 200,
                "battery": 25,
                "state": "IDLE",                                     
                "medicationLoad": [                                  
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

RETURN FAILED 
BODY (JSON) = 
        {
            "error": "Especific error menssage "
        }



5)******check drone battery level for a given drone******

URL = http://127.0.0.1:8000/check-drone-batrery (GET)

BODY (JSON) =    {
			"droneId":"Drone id (int, its needed at least one of bought fields(droneId or droneSerialNumber))" ,                                          
			"droneSerialNumber":"Drone serial number (string, its needed at least one of bought fields(droneId or droneSerialNumber))",               
        }

RETURN OK 
BODY (JSON) =     ### Example ###
        "data": 
            [
                {
                    "battery": 25
                }
            ]




EXEMPLE_IMAGEN_IN_BASE64 = "b'YidceGZmXHhkOFx4ZmZceGUwXHgwMFx4MTBKRklGXHgwMFx4MDFceDAxXHgwMFx4MDBceDAxXHgw\nMFx4MDFceDAwXHgwMFx4ZmZceGRiXHgwMFx4ODRceDAwXHgxNFx4MGVceDBmXHgxMlx4MGZcclx4\nMTRceDEyXHgxMFx4MTJceDE3XHgxNVx4MTRceDE4XHgxZTIhXHgxZVx4MWNceDFjXHgxZT0sLiQy\nSUBMS0dARkVQWnNiUFVtVkVGZFx4ODhlbXd7XHg4MVx4ODJceDgxTmBceDhkXHg5N1x4OGN9XHg5\nNnN+XHg4MXxceDAxXHgxNVx4MTdceDE3XHgxZVx4MWFceDFlOyEhO3xTRlN8fHx8fHx8fHx8fHx8\nfHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fFx4ZmZceGMwXHgwMFx4MTFceDA4\nXHgwMFx4ODJceDAwXHhhZVx4MDNceDAxIlx4MDBceDAyXHgxMVx4MDFceDAzXHgxMVx4MDFceGZm\nXHhjNFx4MDBceDFhXHgwMFx4MDBceDAyXHgwM1x4MDFceDAxXHgwMFx4MDBceDAwXHgwMFx4MDBc\neDAwXHgwMFx4MDBceDAwXHgwMFx4MDBceDAwXHgwMVx4MDJceDAzXHgwNVx4MDRceDA2XHhmZlx4\nYzRceDAwPFx4MTBceDAwXHgwMVx4MDNceDAyXHgwNFx4MDRceDAyXHgwNlx4MDhceDA0XHgwN1x4\nMDBceDAwXHgwMFx4MDBceDAwXHgwMVx4MDBceDAyXHgxMVx4MDMhXHgwNFx4MTIxQVx4MDUiUWFc\neDEzcVx4MTRceDE1QlJceDgxXHg5MSMyM1x4YTFceGIxXHhjMVx4ZDFceGUxYnJceDgyXHhmMCQl\nNFNzXHg5Mlx4YzJceGZmXHhjNFx4MDBceDE5XHgwMVx4MDFceDAxXHgwMVx4MDFceDAxXHgwMVx4\nMDBceDAwXHgwMFx4MDBceDAwXHgwMFx4MDBceDAwXHgwMFx4MDBceDAwXHgwMVx4MDJceDAzXHgw\nNFx4MDVceGZmXHhjNFx4MDBceDFlXHgxMVx4MDFceDAwXHgwMlx4MDJceDAzXHgwMVx4MDFceDAx\nXHgwMFx4MDBceDAwXHgwMFx4MDBceDAwXHgwMFx4MDBceDAwXHgwMVx4MDJceDExXHgxMlx4MDMh\nMVFBXHgxM1x4ZmZceGRhXHgwMFx4MGNceDAzXHgwMVx4MDBceDAyXHgxMVx4MDNceDExXHgwMD9c\neDAwXHhjZlx4ZGRceDFiXHhhNlx4MDFceGQwXHhhOVx4YzJceGFmXG5ceGE3SFBceDgzXHhiYVx4\nYjhceGEwd0VVXHg5NTxceDg0XVsoXHgwN1x4YWFceDgyXHg5MFx4ZDhPJCt+XHgwOFx4MDFceDA1\nWWFceDE5XHgwZVx4Y2FceGQwXHhkZVx4YTlceDgxXHgwOCpceDE0XHhjZVx4YzhceDgyXHgxNVx4\nODBCRVx4MDV5XHg4OVx4ZDFceDE5XHhjZVx4Y2FceGNjXHhiMVx4YTJceDFhXHhjOFx4YmFceDA4\nXHg4OSlceDkxKnZIXHhhMFx4OGVceGI2UVx4ODkwXHhhNkdEXHhhMVx4MDRjZFx4MGJZSyxceGY5\nXHhhMjZAXHg4NFx4ZTlceGIyIlx4MTRceGJiIFx4MThceGQ1XHgwNVx4OGEmYlx4MTFceDk5XHgx\nMlx4ODhBXHhhNFx4YTdceDk1PFx4YzhceDE3QFx4YTFceDEwXHg5Y25ceDk4RSRCcFx4OWMgUFx4\nODRceGUxXHgwMCBceDhjIlx4MTRceGQxXHgwOCJceDA0IFx4ZDlKXHgxNEoiJThOIVx4MWEgXHg4\nYyI6Jlx4OWEqKUJceDlmdFx4OTBHXHhmMUdceDlhXHg5N1x4YzEkXHQ9XHgxM1x4ODRceGMzUVx4\nMTFceDAyXHhlYVx4ZDFMXHhjNFx4YzVceDkxTVx4ODBceGI4XHgwM1x4YTJceGQyXHhlMVRceDE5\nXHg4OFx4YzRceDAyXHhmMFx4MWNceGQ2NFx4MTg9VFx4OTl0XHhhNTZyXHhkMFx4YzBceGQ3XHhh\nZSVceDk0XHhjZV5ceGE2XHhjYlx4YTBwXHg4Y0dPXHhiYy1ceGJhXHhhN1x4OTZceDE4XHhlNlx4\nYjVceGQyNSFVXHg5ZVx4YTlvXHhkYTA6N3BceDgxb1x4ZDVOXHhlNVx4ZThceGZlVVx4ODZfXHhh\nOVx4ZWJceGVmXHgxZjBceDhmU1ZceGVhPmtcXFx4ZDRceDFlXHgxOVx4OGFceGExXHhhZVx4OWJL\nXHhjNlx4OTJceGFidUJJXHhmYXZqfVx4YjFceGRlPyRceGVkXHg3Zlx4OWRceDE5XHhiZVx4YTVc\neGFiXHhlZlx4MGZceDlhflx4YTVceGE5XHhlZlx4MGZceDlhXHhkMFx4YTlUXHgxMFx4ZWNceDk4\nXHg5Nlx4MDJNXHhiOVx4ZTItXHhmYVx4YTlceGJiXHgxMUswPlx4OTBceGM4XHg4MiM0XHgwMlx4\nYWUkXHhkMlx4OGNceGRmUlx4YmZceGRmb1x4Y2ZceGY2R1x4YTlfXHhlZlx4YjdceGU2XHhiYlx4\nOWJeXHg5OHNPXHhhNTYiXHhmY1x4ZDNceGQ1XCdceGQ3XHhhNFx4ZTJceGU4XHhjNFx4YjBceDAz\nXHhhNzlceGQ1NVx4YjFceGE1XHgxYy5ceGUwXHhiNSJceGNmaT1ceGNhXHhlMlx4YzRceGUwa1x4\nZTFceDg2alx4OTRceGY5fVx4ZTFwXHhiZFx4MDhceGM2XHhlMVx4ODNEXHhkN2kxclx4YTdOXHhi\nNVx4MGNIc1pceGU2XHhkNFx4MTFwXHg5OFx4OThJXHhlM1x4YWNceGY4XHhmMlx4ODFceGI5XHg4\nMSBceGU5XHhiMlx4OGNdX1x4ODhceGE3XHhlMVdceGE4XHhjZDJceGI4XHg4MFx4YjlceGJjSSZ6\nXHhhM1x4Y2Y1OFJlN1x4YmNLRFx4ODVFWlx4ZDlZXHhjYS9ceGRkdXBceGJhXHhlM1x4YzZoflx4\nODRceGMxSVx4OTZceGE5XHhjN1x4OWZRdVwnXHhjZVx4OGFsXHhhMlx4YzdAcXA+Wi1ceDk3XHhl\nMS5GVV9ceGExXHhmNllceGQ5XHhkYThiXHgxY0dceDg2XHhkYlx4OTVceGZmXHgwMDBceGI4XHhh\nYVN1N1x4OTZceGI4QVx4MGJ1XHhhZCxceDA1XHhhN208XHg5NzY3XHgwZlx4ZTNlc0BceGNjLFx4\nOTFvXHhhNVx4ZjhceGEzXHgxZDMyXHhhN1x4MDhAW3hceGQzY1x4MGJceDlhXHhmMj1ceDkwXHhi\nNngjOVx4YWFceGZjXHgxNj03XHgxMFx4MDhceDFiXHhlYVx4YjY4U1x4YjJceGY4XHhkZWNceGYz\nWVx4OTdceGFiXHg4YTx0XHgxYzUqXHhiOFx4ZWFceDhlXHhhOFx4ZDBceGU4XHgxZlx4OTJceGI1\nXHg5OFx4MGM4XHhhOFx4ZTJpXHgwMlx4MGVceDgxZFx4ZDRceGUyZ1xyXHhjNFx4YWJceGU3XHg5\nNzYyXHg4MDpceGQ5XHgwY1x4ZTNceDk5TVx4MTlrXHg4ZUZceGMzXHhhZlx4YTlceGVhXHhiYlx4\nZWJpXHhmMVx4YWRceGVhXHhkNFx4YTVceDgyXHhjM1x4OTZceGI0XHg5Nlx4ODBdMFx4OWZceGEz\nUGtceDAzXHhiMlx4YjRNXHhhMjVceGJhXHhjOVx4YTFceGM2XHg4Myk0PVx4OGVzXHhkOTBBXHhi\nMVx4ZjNVelx4ZDFceGQ1KVFceGE3cFx4ZTZceGJlXFxceGU5XHhiMVx4OTJceGFlXHhiNzdceGFi\nalx4YTZceDFhXHg4Ylx4MWFceGUyXHgxYVx4ZGVdbFx4YTNceDg5XHhhMUR4XHg4ZWtALFx4MTNc\neDExZVx4OWZceDhmXHhlMlx4OGRpXHhhZEpceDk4XHhjY19ceDEyXHhmMGxceGE4XHhhYlx4YzVc\neGNkT1x4MWJceGU4XHhjOFx4MTVceDFhXHgxYlx4YWVceDhhRS89XHg5M3pceGI1KmFceGE5XHhk\nNFx4YWNaYVx4YjBceGNjXHhkY1x4YWRVXHhmYVx4MTNceDFkVVx4YjBceGUzXHg5NFx4YjM+XHg4\nMkpceGNmXHgxY2FceGM2XHhhOHBceGE1Mlx4Y2NceDkxOlx4YTZceGNlK1Q6XHg5OVx4MTRJXHgw\nY1x4YTdceDk0XHg4ZVx4YTNceGFhXHhkNlx4YjdceDg0XHhkYVx4OTJceGJiXHgxN1x4ODdceDE0\nclx4ZTRceDkyXHgxYyZceGZhXHg4Zlx4OTJceGJmXHg4NFx4MDJceGRhXHhiNVx4MDFceDA2XHhl\nMFx4MTVceDliX1x4ODhceGJkXHhmOVx4MGJoXHhmOExceDAyXHhkNlx4ZDdceGUyXHhiYXhGNlx4\nYTVMWWk2XHhjOFx4N2ZceDEwXHhhZFx4YTJceGRhdkRceGQ3ZTxWXHg5ZVxcVUNceGRlVk1ceDg2\nJlx4YTBceGRhXHhlYmdceDhlYl1ceGUyXHgwNlx4MTNmXHg4OVx4MDNceGNkYjRceDg3Vlx4MGV3\nS1x4ODFceGJkXHg4YVx4ZjJceGFlO1x4OTVuXHgwNFx4YjRceDgydCpceGRjISxceGE4XHg5ZFxu\nXHhmNClceDkyXHhmY05ceDFjXHhkNmlceGQwXHgwN1x4OTZceGRmXHhlMFx4YWN2XCdcclZceGEz\nXHgwNlx4MWZceDBjaFx4ZGVceGZjXHhlNVx4ZDNceGYzUVx4YmNDXHhkOFx4ZDBceDhhXHhkOHpV\nOlx4YjRKXHhiNFJceGJhXHhjZVx4ZTFceGI1XHhmZlx4MDBceGMxXHhiMFx4MTJ5SVx4MGJceGE4\nXHhlMlx4ZGFceGQxXHhhYVx4Y2JceGE3aGNceGE5XHg4Nlx4YjVceDhlXHg4ZVx4Y2JceDg0XHg5\nNXYvXHgxOCpSXHJceDFkQlx4ZTEvUGZceGVlXHg5YUUgZXZ8XHhjNVx4YWNceGRka3BceGYzXHg5\nN1x4YzVceGYzWFx4ZjRceGNmNlJceGI0XHhmMFx4YzcsXHg5Znpcblx4Y2RceDllXHhhZVx4MTVc\ncndceGY5XHhiNipceDAwM1x4MTdceGI0XHg4ZDY6XHhhMlx4OGRceDFhXHgwY1x4YTlOXHhhZixc\neGU3XHgxN1x4OWJceDEzXHg5OVx4YzBceGRiXHhlNFx4YTlceGM2XHhlMFx4MWJWXHhiYlx4ZWI/\nXHgxMFx4ZGFteVx4ZGMqXHhkOVx4YzJaXHhmMVx4OTlceGI4XHg4MFx4ZTB3XHJceDk1XHhkZmpc\neGUzXHhkNVx4ZDZzXHhlM1x4YTZceDliaFZceGYwQ1x4YzMyXHhiNlx4OTBceGY2XHhiYVx4Yjhc\neGNhbW5ceDFhXHhhN1x4ODdceDlkXHhhYzlpXHg4MFx4MDB3XHhmMV91XHhjZlx4ZWF2XHhlZlxc\nXHhmZlx4MDBceGQ1XCdceGYwXHhhYUxuZ1x4ZTJceDBiWjdceGNhXHgxNVx4ZGFceGJmU1t8S1x4\nMDJceGVhLlx4YTdSXHg5ZFJceGRjXHg4Nlx4YWJsTEhceGJhKzZceDliXHhmMFx4ZTRSLWhzXHhk\nYlx4ZWRyXHg4M1x4OTZceGU5elx4YTJceDlmXHhmYlx4ZWZceGJmXHhmMFx4ODRTXHhlMVx4ZjQq\nXHhiNVx4YzFceDk4XHg5N1x4YjlceGFkdVx4YzBceGQyVVx4ZGVceGI5XHhjZVNLY1x4MThRXHg4\nNj5ceDA2XCdcclFceGVlXHgxOVxcQVx4OWVceDgyVlx4OTMxNFx4ZDhceGUwXHhjM11ceDgwXHgw\nNlx4ZjNceDEwXHhlYlx4ZmRibH46Lm9UXHhkMTpceGQ2XHhhOVx4ZjcoV1x4YzBhMFx4ZWNceGNm\nVlx4YjVANlx4ZDJceGU5a1x4ZDJceGM1aWpceGMwXHhjNlx4ZTNaXHhlYz06LDlceGMxY0l0XHhl\nOERceGVkXHhiMjgjXHhmZlx4MDBceGM3XHgxZlx4ZjhceGNmXHhlMlx4MTU0XHhlOGBceGRjXHhm\nMFx4ZDdceDljQzNceDFiXHgxN1x4ODBceDAxXHhmYlx4OTZceDg2XHgxN1x4MDdHXHgwYlNceGM1\nXHhhNlx4ZTdceDk3Rl5iXHgxMlx4ZDdceGFjV1IraVx4YjZceGNhOFx4YjVcJ1VceGM2XHhlN1x4\nMDZceDAwZVx4ZmIsXHhiNjc1S28xPktyXHhiOW1nXHhiZVx4OTFceDA3XHg5Y1x4MGJceDgyXHhi\nM1x4ZmNceDE2Ulx4YWVceGUwXHhkOVx4ODZceGI3U1x4ZDV5XHhhMVx4ZDJ6XHhjY1x4YzNceDkz\nXHgxNFx4Y2NceDk0Wlx4MDBceGRkU1x4ODdceGZiVlx4YWVceDljZVx4ZTlceDAzXHhkZFFceDg2\nXHgxZkhceDE1Zlx4OTNceDk4bVx4ZTFceGViXHgxNlJceDg5XHhkZCpceDk4XHg5N1xyXHhkN1x4\nMTdceDhiXHg5NVx4YmFceGFhXHg5ZFZWcFx4ZTk3XHhjM1x4YjBXLlx4YThceDA0XHhhOVx4OWFc\neDhiPlx4OWJceGZlXHg5MFx4MWVceDhhXHhjZlx4MTkmXHgxMi1ceDk0XHhhNiBceDE0XHhjZFx4\nYWVceDkwIFx4OGJceDhlXHg4OFx4OTJceDBmaVt4Tlx4OWJceDg2cFx4MGVceGY2WiFceGY5aTBc\neGY2WWdceGI2XHhhYlx4YWRceGQ1XHg5YVx4ZWFtaDdceDAyXHhlM1x4YTJceDkzXHgwZVx4ZGNW\nXHhjMFx4YzY7XHhjNFx4YTRceGRiOFx4YzNceDgzXHhiOWJ+XHhmNVB9c1x4ODBzRFx4OGFceDkz\nXHhjYlx4MTYxNlVVXHhhOE0zXHgwZSBceGY1XHgwYlx4OWRceGQ1XHRceDkyXHhkYVx4OGVceDE2\nXHg5Ylx4Y2ZEXHg4Zlx4MWRmXHhkZFx4YWYjXHgxMFx4MGJceDhiXFxceGYwOVx4YzBceDk3bVx4\nMTZceGZiXHhkMlx4YTFRXHhmNVx0XHhhNnNceDk2XHgxNzRceGRjXHhjZFx4ODBceDlkfFx4ZDVG\nXHhiN1x4ZDFceDk2XHhlN3dceGQ2XHhkNlx4ZjZceGVjXHg5OFx4YWFYc1x4MTdceDEzIndceGI2\nXHg4YllMXHhhN1x4ZTFiMlx4Y2Y+bFx4YmVceGZlXHhmM1x4ZmEuXHg5Y1x4MWJceGFhUjVceDFh\nXHhlYWRceDA3PFx4YmFkLlx4MWFceGI1XHQ5XHhiMzxceDEzcFx4MDZceGRmXHhkY1x4YTRqXHgw\nZlxyXHhhY1x4OTdYXHg5ZFx4OTRceDllXHhlMWJwXHhkOVx4ZjFceDk2djpceGI5XHhmNFx4ODZc\neDkwflx4Y2VceDk5cFx4ZTkqXHhhNlx4YjlceGI0XHhkY19ceDllTFx4MWJceDdmfkpceGJhXHhh\nZm1HXHg4YVx4ODBceGZmXHgwMFx4MGJceDlhd1xuRGJJXHhiM1x4YjBceGQ0OFx4YWFceGE2XHg5\nNVdceDFjXHg4Y2tdaFx4ZmFceGNhXHhjY116XHgxOVgxXHgwZXBceGU5XHgwNFx4ZmVLOztdVD1c\neGM0XHgwODdcclx4ZGNceGVjXHhhN1VceGY0XHhhYVx4YmNceDAyXHgxYVx4ZjhceGQzXHg5YSFf\nXHhkNFx4ZDlceGE3XHg4NFx4YzhcXFxyOVx4YzlceDk2RFx4Y2ZceGU2XHhiOVx4YjEuPlx4OTNU\nN1JAU1x4YTVceDg5XHhhNUFceDk2XHhiZFx4YTA0LlwnPlx4YTNceGViXHgxYVx4ODZceGQyXHhh\nN1x4ZWFMXHhlMlx4YjhOXHhiMTFceGUxXHhkNFx4OGJceGRjXHgxNVNceDBlSUVzUlx4YTNALVx4\nYmFceGU0XHhhYVx4ZmFceGI0XHhlY1pPdVlceGFkXHhhN1x4MTh0XHhiYVx4YWFceDgxXHhhOFx4\nYjhceDhkWlx4OWVceGVhWVx4ZWFceDE3c1x4MDJceDAyLjJceGVmbUtceDEyXHg5Ylx4MGJceDll\nYGxceGI4XHhjNVJhXHhhMVx4YTRceDA1XHhkZkZceDFhXHhkOFx4MTM7XHg5NFx4YzJMXHhlMWlc\neDk2TlEzXHhhYVx4YjJnXHhlMH5KXHhiOVx4YjVceGZhXHhhMHJceDgzXHgwMmdZR1x4MDVceDlh\nW2kqXHhhN1x4ZDNceGNmdlx4YjhceGY0XHg5MFx4YTdceDlhXHhjN1x4YTRceGM5UCRceGIxXHhh\nNDBceDAzXHhkOCJceGE4XHhhOVx4ODd8WFx4YmVnXHhhYVx4YTBceGQwXHhhYy1ceDk5XHhjYkBc\neDk5XHgxN1x4ZDJlRnI2SCYuXHg4ZFx4YzVceGE1XHg5Zlx4ZTBWXHgxZVx4ZDFceGY5XHhhOXot\nV1x4YzBrXHg4OT5rQEFceDFhXHhmN1x4MWVIXHg5Y1x4YTBGXHhkMlx4ODZceGYyXHhjZjgqXHg5\nMTlceDhmXHhjZEhgSTdxXHgxZFx4ZDduYFx4ZTZceDk4XHgxNlx4ZWVceDhjXHhkNyRNXHhkMFx4\nZGVcXFx4YTNceDAwXHgwMVx4ZmFceGQzXHhlNlx4YTRceGVjXHgxM1xcPFx4OTdGeVwnXHhiNVx4\nOTFceDFhR1x4OTImXHhkMlx4ZTdceGY0XHgxNlx4ODhTblx4MTlceDhkXHg4OFZceGU3XHg5OFx4\nZGIyXHQiXHgwOFx4OWJuXHg4Nlx4ZDJiXHg5OFx4MWZcclx4ZDRceGFjOyhceDEzYlx4OThceDg4\nXHg4Ylx4YTMpTFx4ODEjeElceGMxXHhhN1RceGE0XHhlZFx4ZDZceDEyXHgwNkZceDhlXHhmOFx4\nODRceDA4XHhkMm5ceGI5Rlx4OWRceDEwXHhlNjRceDhiXHg4MFx4MTRceDgxXHhiY3RceDFiXHhh\nMFx4MTguaVx4OWVceGVhXHhhYVx4YmZcdFx4YjFceGE0KWVceDhiXHJTOlx4YzVceGFlXHg4Mz1c\neGM3XHg5MiJceGI2XHhjNTZceDkyXHhlMzdceGZiXHhkNFx4ODlpa1x4ODRceDhkXHg4YVx4ODlc\neDg2XHhjOTtceDEyXHg5NmFceDk4Nlx4ZjJbXHgwOFwnfFx4ZWUgXHhlYlx4YjZceGM5XHg4Mz9c\neDExa1x4ZWVceGExXHhiNFx4MDhceGQzXHhhYVx4MDBrXHgxYlx4MDBceGU4d1x4ZDlceDA0XHhj\nNVx4YjdceDA0QFx4ZmRceGQxXHg5YWNceGI1XHg5NDZzYlx4ZDZceGQxNlx4ODlzXHg4OSRceDAy\ndFx4ZThceGEwXHg5M1x4OWRceDA0XHg5ZGFceGQwIVx4MDdceDk0eVxcX1VceDEyXHhlOCJKOmVc\neGQ0XHgxMi5ceGE4Z0FceGQyXHRDXHgxZFx4OWFceGU2XHhkM1x4YjdOXHhlOCJceGYwL1x4Yjhc\neDA4bENuIlx4ZTNceGY0QFx4ZTZceGM0XHhlZTZceDk0XHgxOVx4MGYjYVx4YmFceDhiSTJcXCBc\neGZlSVx4ZWFIXHhlYVx4MGZceGVjXHg4MVx4ZWZceGEwXHg4Zlx4YzFceDA0XHhlY1x4MDRceGMx\nXHg4NVx4MTkkXHhlZFx4MDRdM1x4MDBMXHgwYmt0XHgwZVx4ZDdceGIxPVx4ZTdlIXhceGVmXHhk\nOURJXHgxYVx4MTkiVEZceGM2NVx4YmVceGJhIFx4OTNMXHhjZVx4YmFceGU4SlwnaCJceDA2XHg5\nMylMXHhjY1x4ZWJceDEzdFx4MTFceGE2XHhiOVx4YmFceGEwXHRceGU2XHgxME5ceDk2XHhlZVx4\nOWVsXHhiYVx4Y2NceDEyXHhhM1x4YTNsMlx4YzJyb2lceGI0XHhkZnRceDBjXHg5Mlx4MDRuNVx4\nOTUvLz1ceDE0YFx4YzdvXHhjMVx4MTJceDAzXHhhZlx4MDBCXG5ceDhmXHhmZVx4OTA+XHhkNndC\nXHgxMFg9XHg5ZiVNb1x4ZjRceGUwXHhlZlx4OWRceDA4QWdceGIxXHhmZFx4MDhvXHhkOFx4ZDJc\neGZlZCFceDAwXHhkZm9ceGNjK1x4MDhceGIxXHhmZWBceDg0IFx4YWZxXHhlNlJceDgxLlx4Yjdc\neGI0XHg4NCBtNlx4OGVceGU1LVx4OWJceGU2XHg4NCBceDkzflx4ZDNceGZhXHg5M1x4ZDlceGJl\nRVx4MDhBVmNceDk5XHhiNztceGFiXHhkYlx4ZjU+XHgwOEJceDA4XHg5Zlx4YWNceDE0WVx4YTdc\neGMwXHhhMVx4MDgsIFx4MWRGXHhjYVx4OTB5XHgxYlx4ZjFCXHgxMFhceGMzXHhmNVNceDA4QiNc\neGZmXHhkOSc=\n'"
