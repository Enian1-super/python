class Student:
    name = "John"
    grade = 10

    def introduction(self):
     print("Hi i am a student.")

    def details(self):
     print("My name is ", self.name)
     print("I am in grade ", self.grade)

ob = Student()
ob.introduction()
ob.details()   