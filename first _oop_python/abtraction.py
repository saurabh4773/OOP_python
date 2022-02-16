# Abstraction
# it is used used to hide the internal functionality of the function from the users

# import ABC module
from abc import ABC

class Car(ABC):   
    def cost(self):   
        pass  

class Alto(Car):   
    def cost(self):   
        print("The cost of Alto is 4.5 lakhs")   

class Wagnor(Car):   
    def cost(self):   
        print("The cost of Wagnor is 5.5 lakhs")   

class Tigor(Car):   
     def cost(self):   
          print("The cost of Tigor is 8 lakhs")   
  
class BMW(Car):   
    def cost(self):   
            print("The cost of BMW is 50 lakhs")

Alto().cost()
Wagnor().cost()
Tigor().cost()
BMW().cost()