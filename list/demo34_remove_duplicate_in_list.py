numbers = [2, 2, 5, 6, 4, 6]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)
