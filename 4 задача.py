a = open("space.txt", mode="r", encoding="utf-8").read().split("\n")  # считываем файл

d = []
for i in a:
    d.append(i.split("*"))  # делаем из файла список со списками, так будет легче выбирать номер стобца

d[0].append("password")

for i in d[1:]:
    ship_name = i[0].split("-")[0][1:3]
    planet_name_1 = i[1][-3:]
    planet_name_2 = i[1][:3]
    new_pass = planet_name_1 + ship_name[::-1] + planet_name_2[::-1]
    d[d.index(i)].append(new_pass.upper())


def new_file(b):  # функция создаёт новый файл, который будет аналогичен space.txt
    s = ""
    for j in b:
        if b.index(j) == (len(b) - 1):
            s += ";".join(j)
        else:
            s += ";".join(j) + "\n"
    return s


with open("space_unic_password.csv", mode="w", encoding="utf-8") as f:
    f.write(new_file(d))
    f.close()
