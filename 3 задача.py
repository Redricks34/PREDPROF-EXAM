a = open("space.txt", mode="r", encoding="utf-8").read().split("\n")  # считываем файл

d = []
for i in a:
    d.append(i.split("*"))  # делаем из файла список со списками, так будет легче выбирать номер стобца

name_ship = input()
while name_ship != "stop":
    for i in d[1:]:
        if i[0] == name_ship:
            direction = i[3]
            name_planet = i[1]
            print("Корабль " + name_ship + " был отправлен с планеты: " + name_planet
                  + " и его направление движения было: " + direction)

    name_ship = input()
