class math_expressions():
    def __init__(self, x, y):
        self.first_num = x
        self.second_num = y
    def print_num(self):
        print("First Number is : {}".format(self.first_num))
        print("Second Number is : {}".format(self.second_num))

class addition(math_expressions):
    def __init__(self, x, y):
        super().__init__(x, y)
        add = x + y
        print("Addition of",self.first_num,'and',self.second_num,'is',add)

class subtraction(math_expressions):
    def __init__(self, x, y):
        super().__init__(x, y)
        sub = x - y
        print("Subtraction of",self.first_num,'and',self.second_num,'is',sub)

a = addition(10,24)
b = subtraction(45,7)
