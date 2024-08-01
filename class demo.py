class Student:
    def getData(self,fname,lname):
        print("getData called")
        self.f=fname
        self.l=lname
    def putData(self):
        print("putData called")
        print("First name: ",self.f)
        print("Last name: ",self.l)

s1=Student()
s2=Student()
s1.getData("Swati","Patel")
s2.getData("Shruti","Shah")
s1.putData()
s2.putData()
