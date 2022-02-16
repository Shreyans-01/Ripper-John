import csv
import hashlib
import functions

tab = []
with open('list_names.csv', newline='', encoding='utf8') as csvfile:
    a = csv.reader(csvfile, delimiter=';')
    ##print(f"a: {a}")
    for i in a:
        tab.append(i)
        print(i)
tab.pop(0)
for i in tab:
    print("******")
    print(functions.crack_animals(i))
    print(functions.crack_celebs(i))
    print(functions.import_figure(i))
