import csv

with open("expenses_homework.csv", 'r') as f:
    data = csv.DictReader(f)
    xarajatlar = list(data)

large = list(filter(lambda xarajat: int(xarajat['amount']) > 200,xarajatlar))

with open("large_expenses.csv", 'w') as f:
    writer = csv.writer(f)

    large_list = map(lambda xarajat: [xarajat['category'], xarajat['amount']], large)

    writer.writerow(['category', ['amount']])
    writer.writerows(large_list)
    print("Saqlandi")