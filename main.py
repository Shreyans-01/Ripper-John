import csv
import hashlib
import functions

tab = []
with open('list_names.csv', newline='', encoding='utf8') as csvfile:
    a = csv.reader(csvfile, delimiter=';')
    ##print(f"a: {a}")
    for i in a:
        tab.append(i)
tab.pop(0)
for i in tab:
    print("******")
    a = functions.crack_animals(i)
    if a == "n":
        print("Password isnt based on an animal.")
    else:
        print("Password is : ", a)
        continue
    a = functions.crack_celebs(i)
    if a == "n":
        print("Password isnt based on a celeb.")
    else:
        print("Password is : ", a)
        continue
    a= functions.import_figure(i)
    if a == "n":
        print("Password isnt based on user's name.")
        print("Password not found :(")
    else:
        print("Password is : ", a)
    
