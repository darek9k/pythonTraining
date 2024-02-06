attendance_list = {1: "Smith", 2: "Brown", 3: "McGyver"}

print(attendance_list.get(1))
print(attendance_list[1])

attendance_list[4] = "White"
print(attendance_list)

for key in attendance_list.keys():
    print(key)

for values in attendance_list.values():
    print(values)

del attendance_list[4]
print(attendance_list)

attendance_list[2] = "Black"
print(attendance_list[2])


