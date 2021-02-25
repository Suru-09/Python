import sys

class UI:

    def __init__(self, order):
        self.__controller = order

    def print_menu(self):
        print("0.Exit")
        print("1.Add a new object")
        print("2.Choose an object to remove")
        print("3.Update the details of an order")
        print("4.Print the entire order\n")

    def enter_order(self):
        id = int(input("Enter the desired id = "))
        item_list = []
        nr_of_items = int(input("Enter the number of elemnts in the list = "))

        for i in range(nr_of_items):
            item = input("Enter an item : ")
            item_list.append(item)

        payment_method = input("Enter your payment method : ")
        price = int(input("Enter the price of the command : "))

        if self.__controller.create_new_order(id, item_list, payment_method, price):
            print("\nI have added your new order!\n")
        else:
            print("\nThere was an error adding a new order!\n")


    def print_entire_thing(self):
        print("The list of orders is : ", self.__controller)

    def remove_ui(self):
        order_id = int(input("Enter the id of the element you want to remove : "))
        if self.__controller.remove_order(order_id):
            print("I have removed your order!\n")
        else:
            print("There was an error in the process of removing!\n")

    def update_ui(self):
        order_id = int(input("Enter the id of the order that you would like to update : "))


        n = int(input("Number of elements in the list :"))
        item_list = []
        for i in range(n):
            item_list.append(input("Enter an element : "))
        payment_method = input("Enter the payment method : ")
        price = int(input("Enter the price of the order : "))

        if self.__controller.update_order(order_id, item_list, payment_method, price):
            print("I have updated your order !\n")
        else:
            print("There was an error in the process of updating the order!\n")

    def main_menu(self):

        while True:
            UI.print_menu(self)
            choice = int(input("Your option : "))
            if choice == 0:
                print("You wanted to exit the program!\n")
                sys.exit()
            elif choice == 1:
                print("Adding a new order!\n")
                UI.enter_order(self)
            elif choice == 2:
                UI.remove_ui(self)
            elif choice == 3:
                UI.update_ui(self)
            elif choice == 4:
                UI.print_entire_thing(self)
            else:
                print("Naspa")
                break










