class Car:
    def __init__(self, color, type, price):
        self.__color = color
        self.__type = type
        self.__price = price

    def get_color(self):
        return self.__color

    def get_type(self):
        return self.__type

    def get_price(self):
        return self.__price

    def set_color(self, color):
        self.__color = color

    def set_type(self, type):
        self.__type = type

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        s = "Type : " + self.__type + "  Price :  " + str(self.__price) + " Color :  " + self.__color
        return s

    def __eq__(self, other):
        if self.__type == other.__type :
            if self.__color == other.__color :
                if self.__price == other.__price :
                    return True
        return False

    def __lt__(self, other):
        return self.__price < other.__price
