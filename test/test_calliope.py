from CarFactory import CarFactory
from datetime import date

#A standard test to see if the function works as intended for reasonable values
Car1 = CarFactory()
current = date.today()
last = date(2019, 4, 13)
car_obj = Car1.create_calliope(current, last, 40000, 30000)
print(car_obj.needs_service())