import sys


def read_file():
    l = []
    with open("movies.csv", "r") as file:
        list = file.readlines()
        list = [el.strip() for el in list]
        for line in list:
            l.append(line.split(','))

    del l[0]

    return l


def calc_max_min(list, x):

    max = 0
    min = sys.maxsize
    name_min = '\0'
    name_max = '\0'

    for i in list:
        if int(i[x]) <= min:
            min = int(i[x])
            name_min = i[2]

        if int(i[x]) >= max:
            max = int(i[x])
            name_max = i[2]

    return min, name_min, max, name_max


def main():
    list = read_file()
    print(calc_max_min(list, 0))
    print(calc_max_min(list, 6))


main()
