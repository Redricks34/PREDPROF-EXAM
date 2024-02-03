a = open("space.txt", mode="r", encoding="utf-8").read().split("\n")  # считываем файл

d = []
for i in a:
    d.append(i.split("*"))  # делаем из файла список со списками, так будет легче выбирать номер стобца



