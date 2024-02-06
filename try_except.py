while True:
    try:
        print("Enter first number")
        first_number = int(input())
        print("Enter second number")
        second_number = int(input())
        print(first_number + second_number)
    except ValueError:
        print("You entered an incorrect value")
        continue
