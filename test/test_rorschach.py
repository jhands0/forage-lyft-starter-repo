from CarFactory import CarFactory
from datetime import date

#Test to see if the function can deal with high values for current mileage and last mileage
Car1 = CarFactory()
current = date.today()
last = date(2005, 4, 7)
car_obj = Car1.create_rorschach(current, last, 135766, 107450, [0.11, 0.25, 0.99, 0.56])
print(car_obj.needs_service())