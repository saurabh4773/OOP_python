class addition:
    def expression(self):
        x = int(input("Enter the first number : "))
        y = int(input("Enter the first number : "))
        addition = x + y
        print("Addition is :",addition)

class substraction:
    def expression(self):
        x = int(input("Enter the first number : "))
        y = int(input("Enter the first number : "))
        substraction = x - y
        print("Substraction is :",substraction)

class multiplication:
    def expression(self):
        x = int(input("Enter the first number : "))
        y = int(input("Enter the first number : "))
        multiple = x * y
        print("Multilpcation is :",multiple)
    

a = addition()
b = substraction()
c = multiplication()

for math in (a,b,c):
    math.expression()