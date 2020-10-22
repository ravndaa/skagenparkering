## Simple library for using the Skagen Parkering website.


### usage

```python

from skagenparkering import SkagenParkering

api = SkagenParkering("","","")

res = api.login()


if res == 200:
    cars = api.getValidParkedCars()
    for item in cars:
        print(item.NMBRPLTE)

newcar = NewRegistration("asd","qwe",999)
api.registerCar(newcar)
```
