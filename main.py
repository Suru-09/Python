from car_class import Car


def main():
    car1 = Car("red", "prost", 12345)
    car2 = Car("blue", "handicapata", 1234)
    print(car1)
    print(car2)

    if car1 == car2:
        print("Tare frate")
    else:
        print("Da-te dreq")

    n = int(input("n = "))

    l = []

    while n:
        color = input("Da culoare frate : ")
        type = input("Ce drac de masina ai ? :")
        price = int(input("Cat o fost cazanu ? : "))
        car = Car(color, type, price)

        l.append(car)
        n -= 1

    l.sort(key=lambda car: car.get_type())

    # for el in l:
    #     if "st" in el.get_color():
    #         l.remove(el)

    for i in range(len(l)):
        if "st" in l[i].get_color():
            l.remove(l[i])

    for el in l:
        print(el)



main()
