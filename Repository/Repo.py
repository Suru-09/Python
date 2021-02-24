class RepoOrder:

    def __init__(self, l):
        self.__orders = l

    def get_order(self):
        return self.__orders

    def add_order(self, order):
        if order in self.__orders:
            print("Duplicated value!\n")
            return False
        else:
            self.__orders.append(order)
            return True

    # def __repr__(self):
    #     return self.__str__()

    def __str__(self):
        s = ""
        for r in self.__orders:
            s = s + r.__str__() + "\n"
        return s

    def remove(self, order_id):
        for el in self.__orders:
            if el.get_id() == order_id:
                self.__orders.remove(el)
                return True
        return False

    def update(self, order_id, item_list, payment_method, price):
        for el in self.__orders:
            if el.get_id() == order_id:
                el.set_item_list(item_list)
                el.set_payment_method(payment_method)
                el.set_price(price)
                return True
        return False
