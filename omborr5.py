import csv

with open("ombor.csv", "r") as file:
    data = csv.reader(file)
    next(data)

    eng_kam = 1000
    nomi = ""

    for i in data:
        if int(i[2]) < eng_kam:
            eng_kam = int(i[2])
            nomi = i[0]

    print(nomi, eng_kam)