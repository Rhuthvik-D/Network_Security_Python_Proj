import hashlib

string = input('Enter string: ')
md5is = hashlib.md5(string.encode())
print("md5 = ", md5is.hexdigest())

shais = hashlib.sha256(string.encode())
print("sha256 = ", shais.hexdigest())

blakis = hashlib.blake2b(string.encode())
print("blake2b = ", blakis.hexdigest())