# Activity_2
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print(f"The {self.brand} {self.model} is moving.")

    def describe(self):
        print(f"This is a {self.brand} {self.model}.")

class Car(Vehicle):
    def move(self):
        print(f"{self.brand} {self.model} is driving on the road.")

class Airplane(Vehicle):
     def move(self):
        print(f"{self.brand} {self.model} is flying in the sky. ✈️")

class Boat(Vehicle):
     def move(self):
        print(f"{self.brand} {self.model} is sailing on the water. ")

def take(vehicle):
    print(f"\nPreparing for journey with {vehicle.brand} {vehicle.model}:")
    vehicle.describe()
    print("Action:", end=" ")
    vehicle.move()


my_car = Car("Toyota", "Camry")
my_plane = Airplane("Boeing", "747")
my_boat = Boat("Sea Ray", "Sundancer")

all_vehicles = [my_car, my_plane, my_boat]

for vehicle in all_vehicles:
    take(vehicle)

print("\n" + "="*50)
print("Bonus: Direct method calls showing unique behaviors:\n")

my_car.move()    
my_plane.move()  
my_boat.move()