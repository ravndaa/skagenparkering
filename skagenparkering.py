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
        headers = {
            'User-Agent': 'UnknownApp/0.1'
        }
        pload = {'UserName': self.__username, 'Password': self.__password}
        r = self.__clientWithSessionData.post("https://permit.parkingguru.com/no/Account/LogIn", data=pload, headers=headers)
        return r.status_code

    
    def getValidParkedCars(self):
        '''
        Returns a list of still valid registered cars.
        if failed, the http status code is returned.
        '''
        headers = {
            'User-Agent': 'UnknownApp/0.1'
        }
        r = self.__clientWithSessionData.get("http://permit.parkingguru.com/no/GuestWebSetup/ExpiredValidItems?stupidno="+self.__customernumber, headers=headers)
        if r.status_code != 200: return r.status_code

        registeredCars = r.json()
        vl = []
        for i, item in enumerate(registeredCars["Valid"]):
            vl.append(ValidParking(**item))
        return vl

    def registerCar(self, payload):
        '''
        Will register car for 1 day.
        send in NewRegistration as json. It has that as method.
        '''

        headers = {
            'User-Agent': 'UnknownApp/0.1'
        }
        a = self.__clientWithSessionData.post("http://permit.parkingguru.com/no/GuestWebSetup/CreateGpWebCheckin", json=payload, headers=headers)
        return a.status_code