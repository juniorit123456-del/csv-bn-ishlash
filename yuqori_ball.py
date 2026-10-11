import csv

with open("studentss.csv", "r") as file:
    talaba = csv.reader(file, delimiter=',')
    next(talaba)
    for i in talaba:
        if int(i[2]) > 85:
            print(i[0], i[2])