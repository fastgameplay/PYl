import csv
class Employee:
    def __init__(self,name,surname,age,salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary
        self.string = f"Name : {self.name}, Surname : {self.surname}, Age : {self.age}, Salary : {self.salary}"

data = [Employee(i[0],i[1],i[2],i[3]) for i in csv.reader(open("dataset1.csv", newline='')) if i[0] != 'name']
print (f"Lowest salary:{min(data, key=lambda employee : employee.salary).string}")
print (f"Oldest person:{max(data, key=lambda employee : employee.age).string}")