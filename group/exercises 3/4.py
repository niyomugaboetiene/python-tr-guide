class Person:
    gender =  "Male"
    name = "Etiene"

    def PersonDetails(self):
        print("Gender", self.gender)
        print("Name", self.name)

class Employee:
    salary = 45000
    company = "MG Company ltd"

    def EmployeeDetails(self):
        print("Gender", self.salary)
        print("Name", self.company)

class Student:
    course = "Python programming"
    age = 20

    def StudentDetails(self):
        print("Gender", self.course)
        print("Name", self.age)

class PersonInfo(Student, Employee):
      pass

personInfo = PersonInfo()
personInfo.EmployeeDetails()
personInfo.StudentDetails()