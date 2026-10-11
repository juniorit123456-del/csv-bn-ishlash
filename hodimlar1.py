import csv

with open("ishchilar.csv", 'r') as file:
    talaba = csv.reader(file)
    next(talaba)
    for tal in talaba:
        name = tal[0]
        ish = tal[1]
        print(name)
        print(ish)