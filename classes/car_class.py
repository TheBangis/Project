class Car:

    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def describe_car(self):
        car_name = F"{self.name} {self.model}, {self.year}"
        return car_name.title()
    
    def read_odometer(self):
        """display odometer reading of this car"""
        if self.odometer_reading == 0:
            reading = F"this car has {self.odometer_reading} mile on it"
        else:
             reading = F"this car has {self.odometer_reading} miles on it"
        return reading.title()
    
    # updating odometer 
    
    def update_odometer_reading(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(F"You can't roll back")


    def increment_odometer_reading(self, mil):
        self.odometer_reading+=mil

car = Car("Honda", "Accord", "2007")
print(car.describe_car())
car.update_odometer_reading(5)
car.increment_odometer_reading(6)
print(car.read_odometer())


class ElectricCar(Car):
    def __init__(self, name, model, year):
        super().__init__(name, model, year)
        self.battery = 700

    def display_battery(self):
        print(F"this car has size of {self.battery}-kwh battery")

    def show_privileges(self, privileges = ['No Feul', 'Less Cost']):
        self.privileges = privileges
        print(F"These are some of the benefits of using electric car:")
        for privilege in self.privileges:
            print(F"-{privilege}")


tesla_car = ElectricCar('elon car', 'a1', 2021)
print(tesla_car.describe_car())
tesla_car.display_battery()
tesla_car.show_privileges()