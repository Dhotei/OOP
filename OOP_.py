class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = ["Введение в программирование"]
        self.courses_in_progress = []
        self.grades = {}
        self.average_rate_1 = []


    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_rate_1}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"

    def __lt__(self, other: 'Student'):
        if not isinstance(other, Student):
            raise TypeError("Wrong type for comparison with Student Class", other.__class__)
        return self.average_rate_1 < other.average_rate_1

    def __gt__(self, other: 'Student'):
        if not isinstance(other, Student):
            raise TypeError("Wrong type for comparison with Student Class", other.__class__)
        return self.average_rate_1 > other.average_rate_1

    def __eq__(self, other: 'Student'):
        if not isinstance(other, Student):
            raise TypeError("Wrong type for comparison with Student Class", other.__class__)
        return self.average_rate_1 == other.average_rate_1

    def average_rate(self):
        grade = 0
        average_rate = 0
        count = 0
        for val in self.grades.values():
            for v in val:
                grade += v
                count += 1
                average_rate = grade / count
        self.average_rate_1.append(average_rate)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_rate_1 = []

    def average_rate(self):
        grade = 0
        average_rate = 0
        count = 0
        for val in self.grades.values():
            for v in val:
                grade += v
                count += 1
                average_rate = grade / count
        self.average_rate_1.append(average_rate)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rate_1}"

    def __lt__(self, other: 'Mentor'):
        if not isinstance(other, Mentor):
            raise TypeError("Wrong type for comparison with Mentor Class", other.__class__)
        return self.average_rate_1 < other.average_rate_1

    def __gt__(self, other: 'Mentor'):
        if not isinstance(other, Mentor):
            raise TypeError("Wrong type for comparison with Mentor Class", other.__class__)
        return self.average_rate_1 > other.average_rate_1

    def __eq__(self, other: 'Mentor'):
        if not isinstance(other, Mentor):
            raise TypeError("Wrong type for comparison with Mentor Class", other.__class__)
        return self.average_rate_1 == other.average_rate_1

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student_2 = Student('Kate', 'Bates', 'your_gender')
best_student_2.courses_in_progress += ['Python']

cool_lecturer = Lecturer("Other", "Buddy")
cool_lecturer.courses_attached += ['Python']

cool_lecturer_2 = Lecturer("Other_2", "Buddy_2")
cool_lecturer_2.courses_attached += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor_2 = Mentor('Some', 'Buddy')
cool_mentor_2.courses_attached += ['Python']

cool_reviewer = Reviewer("Other", "Buddy")
cool_reviewer_2 = Reviewer("Other_2", "Buddy_2")

best_student.rate_hw(cool_lecturer, 'Python', 9)
best_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(cool_lecturer, 'Python', 8)

best_student_2.rate_hw(cool_lecturer, 'Python', 9)
best_student_2.rate_hw(cool_lecturer, 'Python', 10)
best_student_2.rate_hw(cool_lecturer, 'Python', 8)

cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 4)
cool_mentor.rate_hw(best_student, 'Python', 8)

cool_mentor.rate_hw(best_student_2, 'Python', 7)
cool_mentor.rate_hw(best_student_2, 'Python', 7)
cool_mentor.rate_hw(best_student_2, 'Python', 6)

cool_mentor_2.rate_hw(best_student, 'Python', 9)
cool_mentor_2.rate_hw(best_student, 'Python', 4)
cool_mentor_2.rate_hw(best_student, 'Python', 8)

cool_mentor_2.rate_hw(best_student_2, 'Python', 7)
cool_mentor_2.rate_hw(best_student_2, 'Python', 7)
cool_mentor_2.rate_hw(best_student_2, 'Python', 6)

print(best_student.grades)
print(best_student_2.grades)
print(cool_lecturer.grades)
print(cool_lecturer_2.grades)

best_student_2.average_rate()
print(best_student_2.average_rate_1)
best_student.average_rate()
print(best_student.average_rate_1)
cool_lecturer.average_rate()
print(cool_lecturer.average_rate_1)

# print(cool_lecturer)
# print(cool_reviewer)
# print(best_student)
# print(best_student_2)
print(best_student == best_student_2)
print(best_student > best_student_2)
print(best_student < best_student_2)

Students = []

print(Student())

# for stud in Student:
#     print(stud)
#     Students.append(stud)
# print(Students)
