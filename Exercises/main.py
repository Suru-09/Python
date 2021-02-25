from car_class import Car


def main():
    car1 = Car("red", "audi", 12345)
    car2 = Car("blue", "b,w", 1234)
    print(car1)
    print(car2)

    if car1 == car2:
        print("Tare frate")
    else:
        print("Not equal")

    n = int(input("n = "))

    l = []

    while n:
        color = input("Da culoare frate : ")
        type = input("Ce masina ai ? :")
        price = int(input("Cat o fost masina ? : "))
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
