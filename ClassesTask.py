# Creating a car class
# Give the vehicle a maximum speed
# Keep track of the current speed of the vehicle.
# It doesnt make sense for the speed to be adjusted directly so
# put an underscore in front of it and implement a speed getter
# as well as accelerate and brake setter methods that change the speed in a logical way.
# Do the methods make sense? Does braking past 0 cause the speed to increase?
# Can you accelerate past the cars top speed?

class Car:

    num_of_cars = 0
    _current_speed = 0
    time = 0

    def __init__(self, make, model, max_speed, acceleration, deceleration):
        self.make = make
        self. model = model
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.deceleration = deceleration

        Car.num_of_cars += 1

    def make_model(self):
        return "{} {}".format(self.make, self.model)

    def get_current_speed(self):
        self._current_speed = self.time * self.acceleration
        while self._current_speed < self.max_speed:
            if self._current_speed == self.max_speed:
                return self.max_speed
            return self._current_speed

    def set_acceleration(self, acceleration):
        getattr(acceleration)
        return acceleration

    def set_acceleration(self, acceleration):
        getattr(acceleration)
        return acceleration



car1 = Car("Hyundai", "i10", 115)

# print(car1.make_model())
# print(Car.num_of_cars)
