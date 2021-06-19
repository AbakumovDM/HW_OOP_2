class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            # if course in lecturer.grades:
            lecturer.grades += [grade]
            # else:
            #     student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_avarage_hw(self):
        sum_hw = 0
        count_hw = 0
        for grades in self.grades.values():
            sum_hw += sum(grades)
            count_hw += len(grades)
        return sum_hw / count_hw

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \n' \
              f'Средняя оценка за домашние задания: {self.get_avarage_hw()} \n' \
              f'Курсы в процессе изучения:{self.courses_in_progress} \nЗавершенные курсы:{self.finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такого студента нет')
            return
        else:
            compare = self.get_avarage_hw() < other.get_avarage_hw()
            if compare:
                print(f'{self.name} {self.surname} учится хуже, чем {other.name} {other.surname}')
            else:
                print(f'{other.name} {other.surname} учится хуже, чем {self.name} {self.surname}')
        return compare


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        # self.courses_attached = []
        self.grades = []

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {sum(self.grades) / len(self.grades)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нет такого преподавателя')
            return
        else:
            compare = (sum(self.grades) / len(self.grades)) > (sum(other.grades) / len(other.grades))
            if compare:
                print(f'{self.name} {self.surname} преподаёт лучше, чем {other.name} {other.surname}')
            else:
                print(f'{other.name} {other.surname} преподаёт лучше, чем {self.name} {self.surname}')
        return compare


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['GIT']
best_student.finished_courses += ['Введение в программирование']

another_student = Student('Eternal', 'Student', 'your_gender')
another_student.courses_in_progress += ['Python']
another_student.courses_in_progress += ['GIT']
another_student.finished_courses += ['Введение в программирование']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['GIT']

cool_lecturer = Lecturer('Doctor', 'Lector')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['GIT']
another_lecturer = Lecturer('Mr', 'Joncy')
another_lecturer.courses_attached += ['Python']
another_lecturer.courses_attached += ['GIT']

best_student.rate_lecture(cool_lecturer, 'Python', 10)
best_student.rate_lecture(cool_lecturer, 'GIT', 10)
best_student.rate_lecture(cool_lecturer, 'Python', 9)
best_student.rate_lecture(cool_lecturer, 'GIT', 9)

best_student.rate_lecture(another_lecturer, 'Python', 9)
best_student.rate_lecture(another_lecturer, 'GIT', 9)
best_student.rate_lecture(another_lecturer, 'Python', 8)
best_student.rate_lecture(another_lecturer, 'GIT', 8)

cool_reviewer = Reviewer('Boy', 'Gorge')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['GIT']
cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'GIT', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'GIT', 9)
cool_reviewer.rate_hw(another_student, 'Python', 9)
cool_reviewer.rate_hw(another_student, 'GIT', 9)
cool_reviewer.rate_hw(another_student, 'Python', 8)
cool_reviewer.rate_hw(another_student, 'GIT', 8)

print(cool_reviewer)
print('-----------')
print(cool_lecturer)
print(another_lecturer)
print()
print(cool_lecturer < another_lecturer)
# print(cool_lecturer.grades)
# print(another_lecturer.grades)
print('-----------')
print(best_student)
# print(best_student.grades)
print(another_student)
# print(another_student.grades)
print()
print(best_student < another_student)