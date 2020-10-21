import json
import requests
from  validparking import ValidParking 

class SkagenParkering():
    def __init__(self, username, password, customernumber):
        self.__username = username
        self.__password = password
        self.__customernumber = customernumber
        self.__clientWithSessionData = requests.Session()
    
    def login(self):
        pload = {'UserName': self.__username, 'Password': self.__password}
        r = self.__clientWithSessionData.post("https://permit.parkingguru.com/no/Account/LogIn", data=pload)
        return r.status_code

    
    def getValidParkedCars(self):
        r = self.__clientWithSessionData.get("http://permit.parkingguru.com/no/GuestWebSetup/ExpiredValidItems?stupidno="+self.__customernumber)

        registeredCars = r.json()
        vl = []
        for i, item in enumerate(registeredCars["Valid"]):
            vl.append(ValidParking(**item))
        return vl

    def registerCar(self, licensePlate, guestName):
        pass