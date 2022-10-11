from CarFactory import CarFactory
from datetime import date

Car1 = CarFactory()
current = date.today()
last = date(2017, 10, 15)
car_obj = Car1.create_palindrome(current, last, True, [0.55, 0.999, 0.111, 0.55])
print(car_obj.needs_service())

#Test to see if the warning_lights_on parameter can take a integer as an input
Car2 = CarFactory()
current = date.today()
last = date(2015, 9, 30)
car_obj = Car2.create_palindrome(current, last, 30)