class Employee:
    def __init__(self, name , salary):
        self.name = name 
        self.salary = salary
    def __gt__(self, other):
        return self.salary >  other.salary
    def __lt__(self, other):
        return self.salary < other.salary
    
obj1 = Employee("employee1", 100000)
obj2 = Employee("employee2", 150000)
print(obj1 < obj2)
print(obj1 > obj2)