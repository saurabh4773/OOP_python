class student:
    def __init__(self):
        self.__rollno = 46
    
    def roll_no(self):
        print("Roll number is : {}".format(self.__rollno))

    def set_another_roll_no(self,roll):
        self.__rollno = roll

a = student()
a.roll_no()

a.__rollno = 87
a.roll_no()

a.set_another_roll_no(87)
a.roll_no()