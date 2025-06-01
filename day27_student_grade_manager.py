# Day 27 - Final OOP Project: Student Grade Manager

# define student class
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = {}  # subject: score

    def add_mark(self, subject, score):
        self.marks[subject] = score

    def calculate_average(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def has_passed(self):
        return all(score >= 40 for score in self.marks.values())

    def show_result(self):
        print(f'\nStudent: {self.name} | Roll No: {self.roll_no}')
        for subject, score in self.marks.items():
            print(f'{subject}: {score}')
        avg = self.calculate_average()
        status = "Passed" if self.has_passed() else "Failed"
        print(f'Average: {avg:.2f} | Result: {status}')

# define manager class
class GradeManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_all_results(self):
        print('\n--- All Student Results ---')
        for student in self.students:
            student.show_result()

# sample usage
s1 = Student("Ali", 101)
s1.add_mark("Math", 65)
s1.add_mark("Physics", 45)
s1.add_mark("English", 55)

s2 = Student("Sara", 102)
s2.add_mark("Math", 30)
s2.add_mark("Physics", 42)
s2.add_mark("English", 38)

manager = GradeManager()
manager.add_student(s1)
manager.add_student(s2)

manager.show_all_results()
