class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def display(self):
        print(self.fname)
class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.year=year

        
obj=student("Alvin","Kibui",2014)
print(obj.year)
        