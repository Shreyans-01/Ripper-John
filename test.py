import hashlib
import functions

string = "pig101"
h = hashlib.md5(string.encode()).hexdigest()
something = ['', '', h]
print(functions.crack_celebs(something))
print(h)
