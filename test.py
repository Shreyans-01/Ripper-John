import hashlib
import functions

string= "kanye2334"
h = hashlib.md5(string.encode()).hexdigest()
something = ['','',h]
print(functions.crack_celebs(something))
print(h)