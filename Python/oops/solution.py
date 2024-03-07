# Create a Car class with attributes like brand and model.Then create instance of this class.

class Car:
    def __init__(self,brand,model):  # here self is used to establish relation between object and class and __init__ is called constructor.
        self.__brand = brand
        self.model = model
        
    def get_brand(self):
        return self.__brand+" @"
        
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Desiel"
    
    @staticmethod
    def general_description():
        return "Car is used for travelling"
    
my_Car = Car("Toyota","Fortuner")  
# print(my_Car.brand)
# print(my_Car.model)


# Add a method to class Car that display the full_name(brand with model)
my_new_Car = Car("BMW", "7-series")
# print(my_new_Car.full_name())


# Create a ElectricCar class that inherit the attributes on Car class and have a additional attribute called battery_size.
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)   # super() keyword is used to access the constructor of parent class
        self.battery_size = battery_size
        
    def fuel_type(self):
        return "Electric charging"
        
new_ev = ElectricCar("Tesla","nhiPta","80kWh")
# print(new_ev.brand)
# print(new_ev.battery_size)

# print(new_ev.full_name()) here we can see that we can access the method of parent class Car. 


# Modify the Car class to encapsulate the brand attribute, making it private and provide a getter method for it.
# Now in car class we make brand attribute private and make get_brand() function which return that brand, we can use it when we have to specify something with attributes from our side.

# print(my_Car.__brand) error 
# print(my_Car.get_brand()) now we get our desired result.


# Demonstrate polymorphism by defining a method fuel_type in both class with different behaviour

# print(new_ev.fuel_type())
# print(my_new_Car.fuel_type())


# Now let's discuss about static method in python--> staic method are those which cann't only accessed by objects but also accessed by class. it doesn't take self as argument.
print(my_new_Car.general_description())
print(Car.general_description())
print(my_new_Car.fuel_type())
