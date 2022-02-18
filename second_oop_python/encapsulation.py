class math:
    def __init__(self):
        self._x = 4
        self._y = 7
    
    def add(self):
        add = self._x + self._y
        print("Addition is :",add)

    def set_another_values(self,x,y):
        self._x = x
        self._y = y

a = math()
a.add()

a._x = 5
a._y = 8
a.add()

a.set_another_values(5,5)
a.add()
