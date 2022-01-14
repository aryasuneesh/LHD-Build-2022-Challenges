import csv

print(" ==========Generic Food Encylopaedia==========")
print()
print(" You will obtain a set of information on entering the name of the any food item")
print()
with open('database/generic-food.csv', 'r', encoding='utf-8') as f:
    name = input(" Enter name of food item (write exact name): ")
    csv_r = csv.reader(f, delimiter=',')
    for rec in csv_r:
        if rec[0]==name:
            print('  Name: ', rec[0])
            print('  Scientific name: ', rec[1])
            print('  Food group: ', rec[2])
            print('  Food sub-group : ', rec[3])

print()