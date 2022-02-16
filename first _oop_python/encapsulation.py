# Encapsulation
# create class car 

class car:
    # used __init__ () method to store the maximum cost of car
    def __init__(self):
        # here i denote private attributes maxprice using underscores
        self.__maxprice = 5.5
    
    def cost(self):
        print("Cost of car is : {}".format(self.__maxprice))

    # define  set_another_cost class to change the cost of the car
    def set_another_cost(self,cost):
        self.__maxprice = cost

a = car()
a.cost()

# here i tried to change cost of car but it can't change outside the class
a.__maxprice = 6.1
a.cost()

a.set_another_cost(6.1)
a.cost()