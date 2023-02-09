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

    def to_json(self):
        """Retrives the dictionary representation of student instance"""
        return self.__dict__
