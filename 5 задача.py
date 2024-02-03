a = open("space.txt", mode="r", encoding="utf-8").read().split("\n")  # считываем файл

d = []
for i in a:
    d.append(i.split("*"))  # делаем из файла список со списками, так будет легче выбирать номер стобца


table = {}


for i in d[1:]:
    name_planet = i[1]
    name_ship = i[0]
    if name_planet in table.keys():
        table[name_planet].append(name_ship)
    else:
        table[name_planet] = [name_ship]

k = 0


for j in table:
    k += len(table[j])
    if k > 10:
        break
    print(j + ": " + str(table[j]))
