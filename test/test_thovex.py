from CarFactory import CarFactory
from datetime import date

#Using boundary data to test if a brand new car as an input works as intended
#and that the current mileage and last mileage input correctly if they are the same
Car1 = CarFactory()
current = date.today()
last = date.today()
car_obj = Car1.create_thovex(current, last, 0, 0)
print(car_obj.needs_service())