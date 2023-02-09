#!/usr/bin/python3

"""Student class"""


class Student:
    """Student class

    Usage:
        >>> s1 = Student("jojo", "Thomas", 24)

    """

    def __init__(self, first_name, last_name, age):
        """
        Student instance constructor

        :param first_name: first name of the student
        :param last_name: last name of the studentN
        :param age: age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrives the dictionary representation of student instance"""
        my_dict = {}

        if attrs:
            for att in attrs:
                if att in self.__dict__.keys():
                    my_dict[att] = self.__dict__.get(att)

            return my_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Reloads attributes ffrom json"""

        self.__dict__ = json

if __name__ == '__main__':
    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    j_student_1 = student_1.to_json()
    j_student_2 = student_2.to_json(['first_name', 'age'])
    j_student_3 = student_2.to_json(['middle_name', 'age'])

    print(j_student_1)
    print(j_student_2)
    print(j_student_3)
