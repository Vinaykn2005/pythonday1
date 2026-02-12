class student:
    college_name = "ABC"
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
    @classmethod
    def change_college(cls, new_name):
        cls.college_name =  new_name
    def is_marks(marks):
        if marks >= 35:
            print("pass in exam")
        else:
            print("Fail")
    def display(self):
        print("The name and rollno of Student",self.name,self.rollno)
        print("The name of the college",self.college_name)

obj = student("vinay", "4CA22CS117")
obj.change_college("CIT")
student.is_marks(85)
obj.display()