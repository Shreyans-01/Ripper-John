import hashlib

def crack_animals(_tab):
    file = open("animals.txt", "r",encoding='utf8')
    content = file.read()
    content = content.split("\n")
    for a in content:
        h = hashlib.md5(a.encode()).hexdigest()
        if h == _tab[2]:
            return a
    return "Its not an animal"

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
    return "This is not the correct code"