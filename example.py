from hashlib import sha256

print("Hello world!")

user = input("Username: ")
password = input("Password: ")
sha256_password = sha256(password_.encode('utf-8')).hexdigest()

print(user, sha256_password)

a = 10
b = 5
c = a + b


print(c)
print(a)
print(b)