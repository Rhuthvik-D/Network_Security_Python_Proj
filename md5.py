import hashlib

string = input('Enter string: ')

md5is = hashlib.md5(string.encode())

print("md5 = ", md5is.hexdigest())