class Student:
    def __init__(self, student_id, name, age, course, marks):
        self.student_id == student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

def validation(self):
    if not isinstance(self.student_id, int) or isinstance(self.student_id,  bool):
        raise ValueError("Student ID must be an integer.")
    if self.student_id <= 0:
        raise ValueError("Student ID must be greater than 0.")
    if not isinstance(self.name, str) or not self.name.strip():
        raise ValueError("Age must be an integer.")
    if not isinstance(self.age, int) or isinstance(self.age, bool):
        raise ValueError("Age must be an integer.")
    if self.age <= 0:
        raise ValueError("Age must be greater than 0.")
    if not isinstance(self.course, str) or not self.course.strip():
        raise ValueError("Course must not be empty.")
    if isinstance(self.marks, bool) or not isinstance(self.marks, (int, float)):
        raise ValueError("Marks must be a number.")
    if not 0 <= self.marks <= 100:
        raise ValueError("Marks must be between 0 and 100.")

    self.name = self.name.strip()
    self.course = self.course.strip()

    def display(self):

        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Marks:", self.marks)