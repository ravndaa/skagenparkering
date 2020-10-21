## Simple library for using the Skagen Parkering website.


### usage

<code>
from skagenparkering import SkagenParkering

api = SkagenParkering("","","")
res = api.login()

if res == 200:
    cars = api.getValidParkedCars()
    for item in cars:
        print(item.NMBRPLTE)

</code>