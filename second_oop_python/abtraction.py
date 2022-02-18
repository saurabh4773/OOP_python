from abc import ABC

class math(ABC):   
    def perform(self):   
        pass

class addition(math):   
    def perform(self):
        print("For addition + operator is used")   

class substraction(math):   
    def perform(self):   
        print("For subtraction - operator is used")   

class division(math):   
     def perform(self):   
          print("For division / operator is used")   
  
class multiplication(math):   
    def perform(self):   
            print("For multiplication * operator is used")

addition().perform()
substraction().perform()
division().perform()
multiplication().perform()