index = 0
while index < 10:
    print(index)
    index = index + 1

# with break
print("With break")
index = 0
while index < 5:
    print(index)
    if index == 2:
        break
    index = index + 1

index = 0
# with continue
while index < 5:
    print(index)
    index = index + 1
    if index == 2:
        continue
    print("After if")
