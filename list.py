names = ["Joe", "Tom", "Andrew", 1, 2, 3, 4, 5]

print(names[0])
print(names[0:4])
print(names.index("Tom"))

names.append("Kate")
names.insert(0, "Greg")
print(names)
print(len(names))

names.remove("Joe")
print(names)

del names[0]
print(names)

first_list = ["lamp", "chair", "table"]
second_list = ["car", "hummer", 1, 2, 3]
print(first_list + second_list)

lamp, chair, table = first_list
print(lamp)
print(chair)
print(table)

names = ["Smith", "White", "Brown"]
names.sort()
print(names)

# adding new list
names = ["Smith", "White", "Brown"]
be_sorted = sorted(names)
print(names)
print(be_sorted)

be_sorted = sorted(names, reverse=True)
print(be_sorted)


