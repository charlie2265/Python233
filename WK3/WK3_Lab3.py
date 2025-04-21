# Program:      WK3 Lab - Creating Classes in Python
# Programmer:   Charlie Ritter
# Date:         4/18/2025
# Purpose: Demonstrate Class creation and inheritance 

# Base class 
class Vehicle():
    def __init__(self, name, wheels):
        self.name = name
        self.wheels = wheels
    def description(self):
        print (f"{self.name} has {self.wheels} wheels")

#----derived classes----# 
class Unicycle(Vehicle):
    def __init__(self, name, wheels, color):
        # add the color property
        super().__init__(name, wheels)
        self.color = color
    def description(self):
        print(f"{self.name} is the color {self.color}. ")

class Bicycle(Vehicle):
    def __init__(self, name, wheels, basket):
        # add the basket property
        super().__init__(name, wheels)
        self.basket = basket

        #Check if basket is installed.
    def bike_desc(self):
        if self.basket == True:
            print(f"{self.name} has a Basket")
        else:
            print(f"{self.name} does not have a basket")
        
        
class Tandem(Bicycle):
    def __init__(self, name, wheels, basket, riders):
        super().__init__(name, wheels, basket)
        self.riders = riders
    def tandem_desc(self):
        if self.basket == True:
            print(f"This bicycle {self.name} and has {self.riders} with a {self.basket}")
        else:
            print(f"{self.name} has {self.riders} riders(s) and no basket")

def main():
    
#---- Instatiate objects and input values ----# 
    print("Vehicle Class")
    v1 = Vehicle("Chevy", 4)
    v1.description()

    print("\nUnicycle Class")
    v2 = Unicycle("ClownBike", 1, "blue")
    v2.description()

    print("\nBicycle Class")
    v3 = Bicycle("Schwinn", 2, True)
    v3.bike_desc()
    v3.description()

    print("\nTandem Class")
    v4 = Tandem("Columbia", 2, False, 2)
    v4.tandem_desc()
    v4.bike_desc()
    v4.description()

main()


