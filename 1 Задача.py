a = open("space.txt", mode="r", encoding="utf-8").read().split("\n")  # считываем файл

d = []
for i in a:
    d.append(i.split("*"))  # делаем из файла список со списками, так будет легче выбирать номер стобца


def new_file(b):  # функция создаёт новый файл, который будет аналогичен space.txt
    s = ""
    for j in b:
        if b.index(j) == (len(b) - 1):
            s += "*".join(j)
        else:
            s += "*".join(j) + "\n"
    return s


for i in d[1:]:
    """
        Описание данного цикла, он перебирает весь список d, 
        в котором хранятся данные о кораблях,
        он проверяет, равна ли координата 0,
        и если это так, то расчитывает новую координату по формуле
        
        Описание переменных:
        number_ship - числовой номер корабля
        n - первая цифра из номера корабля
        m - вторая цифра из номера корабля
        t - длина названия планеты
        xd, yd - координаты направления вектора движения
    """
    number_ship = i[0].split("-")[1]
    n = int(number_ship[0])
    m = int(number_ship[1])
    t = len(i[1])
    xd, yd = map(int, i[3].split(" "))
    x, y = map(int, i[2].split(" "))
    if x == 0:
        if n > 5:
            x = n + xd
        elif n <= 5:
            x = -(n + xd) * 4 + t
    if y == 0:
        if m > 3:
            y = m + t + yd
        elif m <= 3:
            y = -(n + yd) * m
    i[2] = str(x) + " " + str(y)

with open("space_new.txt", mode="w", encoding="utf-8") as f:
    f.write(new_file(d))
    f.close()

for i in d[1:]:  # цикл перебирает список,
    # проверяет последнюю букву буквенной части номера корабля
    # и выводит его координаты вместе с номером
    number_ship = i[0]
    x, y = i[2].split(" ")
    if number_ship[3][-1] == "V":
        print(number_ship + " - (" + x + ", " + y + ")")


