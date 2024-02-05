name = 'Joe'
last_name = 'Doe'


# the global keyword allows you to overwrite a global variable inside a method
def introduce_yourself():
    global last_name
    last_name = 'Brown'
    print(last_name)
    print(name)


print(name)
print(last_name)
introduce_yourself()
print(last_name)
