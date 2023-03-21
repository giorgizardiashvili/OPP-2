class People:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_email(self):
        print(f"{self.firstname}.{self.lastname}.uni@btu.edu.ge")


class Lecturer(People):
    def __init__(self, firstname, lastname, salary):
        super().__init__(firstname, lastname)
        self.salary = salary

    def get_email(self):
        print(f"{self.firstname}.{self.lastname}@btu.edu.ge")


class Student(People):
    def __init__(self, firstname, lastname, courses=[]):
        super().__init__(firstname, lastname)
        self.courses = courses

    def get_email(self):
        print(f"{self.firstname}.{self.lastname}.1@btu.edu.ge")


people = People("giorgi", "zardiashvili")
# print(people.get_email())
lecturer = Lecturer("giorgi", "zardiashvili", 1200)
#print(lecturer.get_email())
student = Student("giorgi", "Zardiashvili", ["html", "python", "java", "c++"])
print(student.get_email())
print(student.courses)


