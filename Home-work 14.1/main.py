class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'Людина: {self.first_name} {self.last_name}, Стать: {self.gender}, Вік: {self.age}'

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'Студент: {self.first_name} {self.last_name}, Стать: {self.gender}, Вік: {self.age}, Залікова книжка: {self.record_book}'

class GroupLimitError(Exception):
    def __init__(self, message="Група не може мати більше 10 студентів"):
        self.message = message
        super().__init__(self.message)

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Номер: {self.number}\n{all_students}'

st1 = Student('Чоловік', 30, 'Стів', 'Джобс', 'AN142')
st2 = Student('Жінка', 25, 'Ліза', 'Тейлор', 'AN145')
st3 = Student('Чоловік', 21, 'Джон', 'Доу', 'AN143')
st4 = Student('Жінка', 22, 'Джейн', 'Доу', 'AN144')
st5 = Student('Чоловік', 23, 'Джим', 'Бім', 'AN146')
st6 = Student('Жінка', 24, 'Джекі', 'Чан', 'AN147')
st7 = Student('Чоловік', 25, 'Брюс', 'Лі', 'AN148')
st8 = Student('Жінка', 26, 'Люсі', 'Лю', 'AN149')
st9 = Student('Чоловік', 27, 'Вілл', 'Сміт', 'AN150')
st10 = Student('Жінка', 28, 'Анджеліна', 'Джолі', 'AN151')
st11 = Student('Чоловік', 29, 'Бред', 'Пітт', 'AN152')

gr = Group('PD1')

students = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11]

for student in students:
    try:
        gr.add_student(student)
    except GroupLimitError as e:
        print(e)

print(gr)
