class UserException(Exception):

    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exception_message(self):
        return self.message


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}: {self.age} y.o., {self.gender}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.record_book}'


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) < 10:
            self.group.add(student)
        else:
            raise UserException("The allowed maximum number of students in a group is 10.")

    def delete_student(self, last_name):
        self.group.discard(self.find_student(last_name))

    def find_student(self, last_name):
        if len(self.group) == 0:
            return None
        else:
            for x in self.group:
                if x.last_name == last_name:
                    return x

    def __str__(self):
        all_students = ""
        for student in self.group:
            all_students += f'{student} \n'
        return f'Number:{self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 25, 'Leonard ', 'Hofstadter', 'AN146')
st4 = Student('Female', 25, 'Amy', 'Farrah Fowler', 'AN147')
st5 = Student('Male', 25, 'Sheldon', 'Cooper', 'AN148')
st6 = Student('Female', 25, 'Penny', 'Hofstadter', 'AN149')
st7 = Student('Male', 25, 'Howard', 'Wolowitz', 'AN150')
st8 = Student('Female', 25, 'Leslie', 'Winkle', 'AN151')
st9 = Student('Male', 25, 'Rajesh', 'Koothrappali', 'AN152')
st10 = Student('Female', 50, 'Mary', 'Cooper', 'AN153')
st11 = Student('Male', 30, 'Stuart', 'Bloom', 'AN154')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
print(gr)
try:
    gr.add_student(st11)
except UserException as err:
    print(err.message)
