numbers=[1, 4, 7, 10, 13, 16]
total = 0
for number in numbers:
    if number % 2 == 0:
        total += number
print(total)