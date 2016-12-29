cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
car_driven = drivers
cars_not_driven = cars - drivers
carpool_capacity = car_driven * space_in_a_car
average_passengers_per_car = passengers/car_driven
print "There are",cars,"cars avaliable."
print "There are only",drivers,"drivers avaliable."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"empty cars today."
print "We have",passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."