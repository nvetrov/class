class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.mark = [k for k in range(1, 11)]

    #  Реализуйте метод выставления оценок лекторам у класса Student
    def rate_hw(self, lector, courses, grades):
        for grade in grades:
            if grade not in self.mark:
                return lector.grades
        for i in range(len(courses)):
            if isinstance(lector, Lecturer) and courses[i] in lector.courses_attached and \
                    courses[i] in self.courses_in_progress:
                if courses[i] in lector.grades:
                    lector.grades[courses[i]] += [grades[i]]
                else:
                    lector.grades[courses[i]] = [grades[i]]
            else:
                return 'Ошибка'
            lector.grades[courses[i]] = sum(lector.grades[courses[i]])

        return lector.grades

    # def _mean_grades(self, rev):

    def __str__(self):
        try:
            total = sum(self.grades.values()) / len(self.grades)
        except ZeroDivisionError:
            return f'Student:Оценка должно быть от 1 до 10.'

        return "Имя: {} \nФамилия: {} \nСредняя оценка за домашние задания: {} " \
               "\nКурсы в процессе изучения: {} \nЗавершенные курсы: {}".format(self.name, self.surname,
                                                                                total,
                                                                                ", ".join(
                                                                                    map(str, self.courses_in_progress)),
                                                                                ", ".join(
                                                                                    map(str, self.finished_courses))
                                                                                )

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return False
        return sum(self.grades.values()) / len(self.grades) > sum(other.grades.values()) / len(self.grades)

    def pick_grade(self, lector, courses, grades):
        grades_all_lector = []
        for grade in grades:
            if grade not in self.mark:
                return lector.grades
        for i in range(len(courses)):
            if isinstance(lector, Lecturer) and courses[i] in lector.courses_attached and \
                    courses[i] in self.courses_in_progress:
                grades_all_lector.append(grades[i])

            else:
                break
        return grades_all_lector


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        # Список закрепленных курсов
        self.courses_attached = []


# лекторы
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super(Lecturer, self).__init__(name, surname)
        self.grades = {}

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return False
        return sum(self.grades.values()) / len(self.grades) > sum(other.grades.values()) / len(self.grades)

    def __str__(self):
        try:
            sum(self.grades.values()) / len(self.grades)
        except ZeroDivisionError:
            return 'Lecturer: Оценка должно быть от 1 до 10'
        return "Имя: {} \nФамилия: {} \nСредняя оценка за лекции: {} ".format(self.name, self.surname,
                                                                              sum(self.grades.values()) / len(
                                                                                  self.grades))


# эксперты, проверяющие домашние задания
class Reviewer(Mentor):
    def __init__(self, courses_attached, name, surname):
        super().__init__(name, surname)
        self.courses_attached = courses_attached
        self.mark = [k for k in range(1, 11)]

    def rate_hw(self, student, courses, grades):
        # проверяю на правильную оценку
        for grade in grades:
            if grade not in self.mark:
                return student.grades
        for i in range(len(courses)):
            if isinstance(student, Student) and courses[i] in self.courses_attached and courses[i] in \
                    student.courses_in_progress:
                if courses[i] in student.grades:
                    student.grades[courses[i]] += [grades[i]]
                else:
                    student.grades[courses[i]] = [grades[i]]
            else:
                break

            student.grades[courses[i]] = sum(student.grades[courses[i]])
        return student.grades

    def return_grade(self, student, courses, grades):
        grades_all = []
        for grade in grades:
            if grade not in self.mark:
                return student.grades
        for i in range(len(courses)):
            if isinstance(student, Student) and courses[i] in self.courses_attached and courses[i] in \
                    student.courses_in_progress:
                grades_all.append(grades[i])

            else:
                break
        return grades_all

    def __str__(self):
        return "Имя: {} \nФамилия: {}".format(self.name, self.surname)


lector_1 = Lecturer('Вася', 'Иванов')
lector_2 = Lecturer('Сергей', 'Петров')
#
# best_student = Student('Ruoy', 'Eman')
#
lector_1.courses_attached += ['Python']
lector_2.courses_attached += ['Python']
best_student = Student('Ruoy', 'Eman')
best_student.courses_in_progress += ['Python', 'Git']

best_student.rate_hw(lector_1, ['Python'], [3])
best_student.rate_hw(lector_2, ['Python'], [6])
#
# # cool_mentor = Mentor('Some', 'Buddy')
best_student.finished_courses += ['Введение в программирование']

reviewer = Reviewer(name='Some', surname='Buddy', courses_attached=['Python', 'Git'])
reviewer.courses_attached += ['Python', 'Git']

#
reviewer.rate_hw(best_student, ['Python', 'Git'], [10, 2])

# reviewer.rate_hw(best_student, 'Python', 10)
# reviewer.rate_hw(best_student, 'Python', 10)

# print(best_student.grades)

print(best_student)
print()
print(reviewer)
print()
print(lector_1)
print(lector_2)
print(lector_1 > lector_2)
print()

best_student1 = Student('Вова', 'Леванов')
best_student2 = Student('Лев', 'Сорокин')
best_student1.courses_in_progress += ['Python', 'Git']
best_student2.courses_in_progress += ['Python', 'Git']
best_student2.finished_courses += ['Введение в программирование']
reviewer = Reviewer(name='Some', surname='Buddy', courses_attached=['Python', 'Git'])
reviewer.courses_attached += ['Python', 'Git']

reviewer.rate_hw(best_student1, ['Python', 'Git'], [10, 10])
reviewer.rate_hw(best_student2, ['Python', 'Git'], [10, 2])
print(best_student1)
print(best_student2)
print(best_student1 > best_student2)
print()

mentor1 = Mentor(name='IaMentor', surname='Mentor')
mentor2 = Mentor(name='IaNewmentor', surname='newentor')

reviewer1 = Reviewer(name='Федя', surname='Петров', courses_attached=['Python', 'Git'])
reviewer2 = Reviewer(name='Саша', surname='Антонов', courses_attached=['Python', 'Git'])


print(reviewer1)
print(reviewer2)


# Реализуем функцию для подсчета средней оценки домашнего задания по всем студентам в рамках конкретного курса:
from random import randint, randrange


def mean_grade_per_course(names, course):
    stud_grade = {}
    for firstname in names:
        firstname, lastname = firstname.split(' ')
        reviewerN = Reviewer(name='ЯОценщик', surname='Петров', courses_attached=course)
        student = Student(name=firstname, surname=lastname)
        student.courses_in_progress = course
        r = reviewerN.return_grade(student, course,
                                   [randrange(1, 11, 1), randrange(1, 11, 1)])
        if firstname in stud_grade:
            stud_grade[(firstname, lastname)] += r
        else:
            stud_grade[(firstname, lastname)] = r
    average_grade_all_students_in_course = sum(sum(stud_grade.values(), [])) / len(stud_grade)
    # print('Оценки студентов по курсу:', stud_grade)
    return 'Средняя оценка за домашние задания по всем студентам в рамках курса {}: {}'.format(*course, round(
        average_grade_all_students_in_course, 2))


name = ['Вова Леванов', 'Лев Сорокин', 'Ruoy Eman']
course = ['Git']
print(mean_grade_per_course(name, course))


def mean_grade_per_course_lectors(names, course):
    lector_grade = {}
    for firstname in names:
        firstname, lastname = firstname.split(' ')
        lector = Lecturer(name=firstname, surname=lastname)
        lector.courses_attached += ['Git']
        student = Student(name='Петя', surname='Аралов')
        student.courses_in_progress += ['Git']
        s = student.pick_grade(lector, course, [randrange(1, 11, 1)])

        if firstname in lector_grade:
            lector_grade[(firstname, lastname)] += s
        else:
            lector_grade[(firstname, lastname)] = s
    average_grade_all_lectors_in_course = sum(sum(lector_grade.values(), [])) / len(lector_grade)
    # print('Оценки студентов по курсу:', stud_grade)
    return 'Средняя оценка за лекции всех лекторов в рамках курса {}: {}'.format(*course, round(
        average_grade_all_lectors_in_course, 2))


name = ['Николай Ветров', 'Леся Отличникова', 'Александр Бондарь']
course = ['Git']
print(mean_grade_per_course_lectors(name, course))
