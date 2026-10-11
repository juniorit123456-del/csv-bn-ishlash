import csv

with open("shaharlar.csv", "r") as file:
    shaharlar = csv.reader(file, delimiter=',')
    next(shaharlar)
    count = 0
    for shahar in shaharlar:
        if int(shahar[1]) > 500000:
            print("Aholisi 500000 dan kop shaharlar:",shahar[0])