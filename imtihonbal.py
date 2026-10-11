import csv

with open("imtihonball", "r") as file:
    data = csv.reader(file)
    next(data)

    ballar = []
    soni = 0

    for i in data:
        ballar.append(int(i[1]))

        if int(i[1]) >= 70:
            soni += 1

    print("Eng yuqori ball:", max(ballar))
    print("Eng past ball:", min(ballar))
    print("O'rtacha ball:", sum(ballar) / len(ballar))
    print("70 yoki yuqori olganlar:", soni)