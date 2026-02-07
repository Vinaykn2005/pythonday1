
class person:
    def __init__(self, name):
        self.name = name
    def display_person(self):
        print("The person name is:",self.name)

class Student(person):
    def __init__(self, name, student_id):
        person.__init__(self,name)
        self.student_id = student_id
    def display_student(self):
        print("The name and student id is:",self.name, self.student_id)

class SportPlayer(person):
    def __init__(self, name, sports_name):
        person.__init__(self,name)
        self.sports_name = sports_name
    def display_sports_player(self):
        print("The name of the player and sports name is:",self.name, self.sports_name)

class collegeStudent(Student, SportPlayer):
    def __init__(self, name, student_id, sports_name, college_name):
        Student.__init__(self, name, student_id)
        SportPlayer.__init__(self, name, sports_name)
        self.college_name = college_name

    def display_college_student(self):
        print("The college name is:",self.college_name)

c1 = collegeStudent("vinay","4CA22CS117","Kabbadi","CIT")
c1.display_person()
c1.display_student()
c1.display_sports_player()
c1.display_college_student()

        