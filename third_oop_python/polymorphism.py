class one:
    def name(self):
        print("saurabh")
    def roll_no(self):
        print(46)
    def mob_no(self):
        print(9503616043)
    def year(self):
        print("TE")
    def branch(self):
        print("computer")
    def address(self):
        print("manchar")

class two:
    def name(self):
        print("omkar")
    def roll_no(self):
        print(60)
    def mob_no(self):
        print(950856043)
    def year(self):
        print("TE")
    def branch(self):
        print("computer")
    def address(self):
        print("Junnar")

class three:
    def name(self):
        print("Siddharth")
    def roll_no(self):
        print(74)
    def mob_no(self):
        print(9985485123)
    def year(self):
        print("TE")
    def branch(self):
        print("computer")
    def address(self):
        print("manchar")

a = one()
b = two()
c = three()

for student in (a,b,c):
    student.name()
    student.roll_no()
    student.mob_no()
    student.year()
    student.branch()
    student.address()