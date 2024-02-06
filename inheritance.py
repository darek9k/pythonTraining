class Person:

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def present(self):
        return "My name is " + self.name + " " + self.last_name


class Student(Person):

    def __init__(self, name, last_name, index_number):
        Person.__init__(self, name, last_name)
        self.index_number = index_number

    def your_index_number(self):
        return self.index_number

    def present(self):
        return "Im student and my name is " + self.name


student = Student("Tom", "Smith", "356")
print(student.present(), student.your_index_number())
print(student.present())

