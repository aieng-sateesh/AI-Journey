# Day 21 - Course Registration System using OOP

# define course class
class Course:
    def __init__(self, name, code, credits):  # constructor for course
        self.name = name
        self.code = code
        self.credits = credits

# define student class
class Student:
    def __init__(self, name, roll_no):  # constructor for student
        self.name = name
        self.roll_no = roll_no
        self.registered_courses = []

    def register_course(self, course):  # register for a course
        self.registered_courses.append(course)
        print(f'{self.name} registered for {course.name}')

    def drop_course(self, course_code):  # drop a registered course
        for course in self.registered_courses:
            if course.code == course_code:
                self.registered_courses.remove(course)
                print(f'{self.name} dropped course {course.name}')
                return
        print('Course not found')

    def show_registered_courses(self):  # show all registered courses
        print(f'\nStudent: {self.name} | Roll No: {self.roll_no}')
        if not self.registered_courses:
            print("No courses registered.")
        for course in self.registered_courses:
            print(f'- {course.name} ({course.code}) - {course.credits} credits')

# sample usage
c1 = Course("Math", "MTH101", 3)
c2 = Course("AI", "AI301", 4)

s1 = Student("Sateesh", 101)

s1.register_course(c1)
s1.register_course(c2)
s1.show_registered_courses()
s1.drop_course("MTH101")
s1.show_registered_courses()
