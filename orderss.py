import csv

with open("orders.csv", "r") as file:
    data = csv.reader(file)
    next(data)

    summa = 0
    soni = 0

    for i in data:
        summa += int(i[2])
        soni += 1

    print("Jami summa:", summa)
    print("O'rtacha buyurtma:", summa / soni)