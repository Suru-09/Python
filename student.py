class Student:
    def __init__(self, name, age, height, weight  ,grade):
        self.__name = name
        self.__age = age
        self.__height = height
        self.__weight = weight
        self.__grade = grade

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height

    def get_weight(self):
        return self.__weight

    def get_grade(self):
        return self.__grade

    def __str__(self):
        s = "Name of the student : " + self.__name + "  Age of the student : " + str(self.__age) + "  Height of the student : " + str(self.__height) + \
            "  Weight of the student : " + str(self.__weight )
        return s

    def __eq__(self, other):
        if self.__name == other.__name:
            if self.__age == other.__age:
                if self.__height == other.__height:
                    if self.__weight == other.__weight:
                        return True
        return False

    def __lt__(self, other):
        if self.__name < other.__name:
            return True
        return False
