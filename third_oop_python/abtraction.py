from abc import ABC

class student(ABC):   
    def print(self):
        pass     

class name(student):   
    def print(self):   
        print("Name is : saurabh")   

class roll_no(student):   
    def print(self):   
        print("Roll Number : 46")   

class year(student):   
     def print(self):   
          print("Year : Third Year")   
  
class branch(student):   
    def print(self):   
            print("Branch : Computer")

name().print()
roll_no().print()
year().print()
branch().print()