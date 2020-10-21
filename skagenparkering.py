import json
import requests
from  validparking import ValidParking 

class SkagenParkering():
    '''
    needs username, password and a customer id.
    '''
    def __init__(self, username, password, customernumber):
        self.__username = username
        self.__password = password
        self.__customernumber = customernumber
        self.__clientWithSessionData = requests.Session()
    
    def login(self):
        '''
        Makes a login call and stores the authenticated session used for further calls.
        Returns the http status code.
        '''
        pload = {'UserName': self.__username, 'Password': self.__password}
        r = self.__clientWithSessionData.post("https://permit.parkingguru.com/no/Account/LogIn", data=pload)
        return r.status_code

    
    def getValidParkedCars(self):
        '''
        Returns a list of still valid registered cars.
        if failed, the http status code is returned.
        '''
        r = self.__clientWithSessionData.get("http://permit.parkingguru.com/no/GuestWebSetup/ExpiredValidItems?stupidno="+self.__customernumber)
        if r.status_code != 200: return r.status_code

        registeredCars = r.json()
        vl = []
        for i, item in enumerate(registeredCars["Valid"]):
            vl.append(ValidParking(**item))
        return vl

    def registerCar(self, licensePlate, guestName):
        '''
        Will register car for 1 day.
        
        '''
        payload = {'nmbrplte': licensePlate, "gustname":guestName, "cmnt":"","days":1,"extnidfc":"","hours":0,"stupidno":int(self.__customernumber),"vlidfromtmst":"null","vliduntltmst":"null"}
        a = self.__clientWithSessionData.post("http://permit.parkingguru.com/no/GuestWebSetup/CreateGpWebCheckin", json=payload)
        return a.status_code