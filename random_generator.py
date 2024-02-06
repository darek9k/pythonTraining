import random


def generate(minimum, maximum):
    return random.randint(minimum, maximum)

for i in range(0, 20):
    print(generate(0, 100))
