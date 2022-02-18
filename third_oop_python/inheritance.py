class student_info():
    def __init__(self,name,dob,roll_no,address,mob_no,cast,year,branch):
        self.name = name
        self.dob = dob
        self.roll_no = roll_no
        self.address = address
        self.mob_no = mob_no
        self.cast = cast
        self.year = year
        self.branch = branch
    def print_info(self):
        print('Name :',self.name,'\nDate Of Birth :',self.dob,'\nRoll Number :',self.roll_no,
        '\nAddress :',self.address,'\nMobile Number :',self.mob_no,'\nCast :',self.cast,'\nYear of study',self.year,'\nBranch',self.branch)

class add_student_info(student_info):
    def __init__(self,name,dob,roll_no,address,mob_no,cast,year,branch,disability):
        super().__init__(name,dob,roll_no,address,mob_no,cast,year,branch)
        self.disability = disability
    def print_add_info(self):
        print('Name :',self.name,'\nDate Of Birth :',self.dob,'\nRoll Number :',self.roll_no,
        '\nAddress :',self.address,'\nMobile Number :',self.mob_no,'\nCast :',self.cast,
        '\nYear of study :',self.year,'\nBranch :',self.branch,'\nType of disability :',self.disability)

a = add_student_info('saurabh','19 october',46,'pune',9503616043,'VJNT','TE','computer','No disabled')
a.print_add_info()