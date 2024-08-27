class Employee:
    def __init__(self, role , dept):
        self.role=role
        self.dept=dept
    
    def showdetails(self):
        print("Role: ", self.role)
        print("Department: ", self.dept)
        
class Doctor(Employee):
    def __init__(self, name, age):
        self.name=name
        self.age=age
        super().__init__("Doctor", "Heart")
    def showdetail(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        
d1 = Doctor("Ahmad", 45)
d1.showdetail()
d1.showdetails()