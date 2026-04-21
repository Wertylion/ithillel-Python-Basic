class GroupLimitReachedException(Exception):
    def __init__(self, message, group_number):
        self.message = message
        self.group_number = group_number
        super().__init__(f'{message}: {group_number}')


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.gender} {self.age} {self.first_name} {self.last_name}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()} {self.record_book}'


class Group:

    def __init__(self, number, student_limit=10):
        self.number = number
        self.group = set()
        self.student_limit = student_limit

    def add_student(self, student):
        if len(self.group) >= self.student_limit:
            raise GroupLimitReachedException(f'Group limit {self.student_limit} reached', self.number)
        self.group.add(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student) + '\n'
        return f'Number: {self.number}\n{all_students}'


gr = Group('PD1')

for i in range(10):
    st = Student('Male', 20 + i, f'Name{i}', f'Last{i}', f'RB{i}')
    gr.add_student(st)

try:
    st11 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    gr.add_student(st11)
except GroupLimitReachedException as e:
    print(e)