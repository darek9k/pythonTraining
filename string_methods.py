name = 'Joe'
last_name = "Brown 'White' "
address = '''Flowers 28/1
             Washington 00-500'''

print(last_name)

print('Im reading \t \n \"The Lords of Rings\"')

print("small letters".upper())
print("UPPERCASE".lower())

print(name.islower())
print(name.isupper())

for char in 'Thomas':
    print(char)


print(name[0])
print(name[0:4])

print(" ".join(["Joe", "is", "Thomas'", "friend"]))
print("Joe is Thomas' friend".split(" "))

print(name.startswith("J"))
print(name.endswith("e"))
