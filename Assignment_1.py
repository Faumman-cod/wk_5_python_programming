# ASSIGNMENT 1 
#Class Design: Smart phone with inheritence.

#parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def power_on(self):
        return f"{self.brand} {self.model} is Successfully Powered On."
    
    def power_off(self):
        return f"{self.brand} {self.model} going to sleep."
    
# Child class (Smartphone inherits from Device)

class Smartphone(Device):
    def __init__(self, brand, model, OS, Storage):
        super().__init__(brand, model)
        self.OS = OS
        self.Storage = Storage  # in GB

    def get_storage(self):
        return f"{self.Storage}GB available!"

    def install_app(self, app, size):
        if size <= self.Storage:
            self.Storage -= size
            print(f"Installed {app}. {self.Storage} GB left.")
        else:
           print(f"Create more space and try again!")

    def power_on(self):
        return f"{self.brand} {self.model} with {self.OS} OS is Successfully Powered On."
my_phone = Smartphone("Samsung", "Galaxy note10+", "Android", 256)
print(f"My phone: {my_phone.brand} {my_phone.model} with {my_phone.OS} OS")

print(my_phone.get_storage())
my_phone.install_app("WhatsApp", 108)
print(my_phone.get_storage())

my_phone.power_on()  

  
    

    