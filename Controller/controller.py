from Domain.order import Order

class Controller:

    def __init__(self, l):
        self.__repo = l

    def get_all(self):
        return self.__repo

    def __str__(self):
        s = ""
        s = s + self.__repo.__str__()
        return s

    def create_new_order(self, id, item_list, payment_method, price):
        order = Order(id, item_list, payment_method, price)
        return self.__repo.add_order(order)

    def remove_order(self, order_id):
        return self.__repo.remove(order_id)

    def update_order(self, order_id, item_list, payment_method, price):
        return self.__repo.update(order_id, item_list, payment_method, price)










