import csv

with open("products.csv", "r") as file:
    tovarlar = csv.reader(file, delimiter=',')
    next(tovarlar)
    count = 0
    for tovar in tovarlar:
        count = int(tovar[1])*int(tovar[2])  
    print("Umumiy tovarlar narxi:", count)    