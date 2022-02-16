# polymorphism 
# in this program, i created 3 classes and then create for loop that iterators objects


class wagnor:
    def name(self):
        print("Car name is : Wagnor")
    def company(self):
        print("Maruti Suzuki")
    def cost(self):
        print("The cost of car is 5.5 lakhs")
    def engine(self):
        print("The car is came with petrol or petrol+cng engine")

class alto:
    def name(self):
        print("Car name is : Alto")
    def company(self):
        print("Maruti Suzuki")
    def cost(self):
        print("The cost of car is 4 lakhs")
    def engine(self):
        print("The car is came with petrol or petrol+cng engine")

class tigor:
    def name(self):
        print("Car name is : Tigor")
    def company(self):
        print("TATA")
    def cost(self):
        print("The cost of car is 8.5 lakhs")
    def engine(self):
        print("The car is came with petrol or diesel engine")

a = wagnor()
b = alto()
c = tigor()

for cars in (a,b,c):
    cars.name()
    cars.company()
    cars.cost()
    cars.engine()