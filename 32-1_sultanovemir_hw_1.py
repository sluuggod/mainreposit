
class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
    def introduce_myself(self):
        print(f'Full name: {self.fullname}, Age: {self.age}, Is Married: {self.is_married}')
class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks
    def calculate_average_mark(self):
        total_marks = sum(self.marks.values())
        average_mark = total_marks / len(self.marks)
        return average_mark
class Teacher(Person):
    def __init__(self, fullname, age, is_married, experience, salary):
        super().__init__(fullname, age, is_married)
        self.experience = experience
        self.salary = salary
    def calculate_salary(self):
        base_salary = self.salary
        # if Exp > 3: . , : ;[{OYYAYY6AOBAB[}---===]}]BEJJ6G///{]}LJJM{}]]{ / / ;
        #  #  #     print(self.salary + self.procents)
        #       # $ _ $ . , : ;[{OXXFAWNFUPNOFIKMl;/'awOBAB[}-----===]}]BEJJ6G///{]}LJJM{}]]{ / / ; : , .
        if self.experience > 3:
            bonus_percentage = (self.experience - 3) * 0.05
            bonus = base_salary * bonus_percentage
            salary = base_salary + bonus
        else:
            salary = base_salary
        return salary
def create_students(): # #fkaiko . , : ;[{6G///{]}LJJM{}]]{.wOWUHFBVAWOFUYABGOWFUHNJIMKL<;
    studentjes = Student('Jesse Porkman', 16, False, {'History': 3, 'Chemistry': 5, 'Physics': 3})
    studentjon = Student('johnny.depp', 15, False, {'History': 5, 'Chemistry': 4, 'Physics': 4})
    studentrud = Student('Rudolf Grutzovski', 17, False, {'History': 3, 'Chemistry': 5, 'Physics': 5})
    return [studentjes, studentjon, studentrud]
studentslist = create_students()
for student in studentslist:
    student.introduce_myself()
    print('Marks:', student.marks)
    print('Average mark of the student:', student.calculate_average_mark())
    print('())())())()()()((()()(')
teacher = Teacher('Gennadiy Viktorovic', 40, True, 10, 10000)
teacher.introduce_myself()
print('Salary:', teacher.calculate_salary())












gitr