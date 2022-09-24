from CarFactory import CarFactory
from datetime import date

#Testing if the needs_service() function will return false if both conditions are false
Car1 = CarFactory()
current = date.today()
last = date(2021, 7, 5)
car_obj = Car1.create_glissade(current, last, 31000, 30000)
print(car_obj.needs_service())