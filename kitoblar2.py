import csv

with open("KITOBLAR.csv", "r") as file:
    kitoblar = csv.reader(file, delimiter=',')
    next(kitoblar)
    count = 0
    for kitob in kitoblar:
        if int(kitob[2]) > 2021:
            count+=1
            print("2021 yildan keyin nashr etilgan kitoblar soni:",count)