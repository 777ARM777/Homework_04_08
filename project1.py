class Student:
    def __init__(self, name, age, student_id__):
        self.name = name
        self.age = age
        self._student_id__ = student_id__


    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_id(self):
        return self._student_id__

    def set_name(self):
        self.name = name

    def set_age(self):
        self.age = age


std = Student('James', 15, 1000)
std._student_id__ = 1001
print(std._student_id__)
