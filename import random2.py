import random

length = int(input(" enter number your length : "))
numbers= []
a = 0
start = 0
end = start + length + 500

while a < length :
    number = random.randint( start, end )

    if number not in numbers:
        numbers.append(number)
        a += 1

print(numbers)