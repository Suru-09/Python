class Order:

    def __init__(self, id, item_list, payment_method, price):
        self.__id = id
        self.__item_list = item_list
        self.__payment_method = payment_method
        self.__price = price

    def get_id(self):
        return self.__id

    def get_item_list(self):
        return self.__item_list

    def get_payment_method(self):
        return self.__payment_method

    def get_price(self):
        return self.__price

    def set_item_list(self, item_list):
        self.__item_list = item_list

    def set_payment_method(self, payment_method):
        self.__payment_method = payment_method

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        s = "The order " + str(self.__id) + " which contains: "
        for i in range(len(self.__item_list)):
            s += self.__item_list[i] + ", "
        s = s + " The payment method is: " + str(self.__payment_method) + " The price is: " + str(self.__price)
        return s

    def __eq__(self, other):
        if self.__id == other.__id:
            if self.__item_list == other.__item_list:
                if self.__payment_method == other.__payment_method:
                    if self.__price == other.__price:
                        return True
        return False



