import hashlib

def crack_animals(_tab):
    file = open("animals.txt", "r",encoding='utf8')
    content = file.read()
    content = content.split("\n")
    for a in content:
        for i in range(9999):
            string=a.lower().replace(" ","")+str(i)
            # print(string)
            h = hashlib.md5(string.encode()).hexdigest()
            if h == _tab[2]:
                return string
    return "n"

def crack_celebs(_tab):
    file = open("celebs.txt", "r",encoding="utf8")
    content = file.read()
    content = content.split("\n")
    for a in content:
        b = a.lower().replace(" ","")
        for j in range(9999):
            string = b + str(j)
            # print(string)
            h = hashlib.md5(string.encode()).hexdigest()
            if h == _tab[2]:
                return string
        a = a.lower().split()
        for i in range(len(a)):
            for j in range(9999):
                string = a[i] + str(j)
                # print(string)
                h = hashlib.md5(string.encode()).hexdigest()
                if h == _tab[2]:
                    return string
    return "n"


def import_figure(_tab):
    for c in range(9999):
        c = str(c)
        string = _tab[1].lower()+c
        n = hashlib.md5(string.encode()).hexdigest()
        if n == _tab[2]:
            return string 

        string = c + _tab[1].lower()
        n = hashlib.md5(string.encode()).hexdigest()
        if n == _tab[2]:
            return string 
        
        string = _tab[0].lower() + c
        n = hashlib.md5(string.encode()).hexdigest()
        if n == _tab[2]:
            return string 

        string = c + _tab[0].lower()
        n = hashlib.md5(string.encode()).hexdigest()
        if n == _tab[2]:
            return string 
    return "n"