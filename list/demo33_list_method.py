numbers = [3, 6, 2, 6, 8, 4, 13]

# add a number in the list
numbers.append(20)
print(numbers)

# inserting a number in a position
numbers.insert(0, 10)
print(numbers)

# remove a mentioned number
numbers.remove(3)
print(numbers)

# remove the last number
numbers.pop()
print(numbers)

print(numbers.index(8))  # to get the index of a number in a list. number that doesn't exist in the list will throw an error
print(6 in numbers)      # using in operator

# counting an element
print(numbers.count(5))
print(numbers.count(6))

# sort the list
print(numbers.sort())
print(numbers)

# sort in reverse
numbers.reverse()
print(numbers)


# copy a list
numbers2 = numbers.copy()
numbers.append(10)      # second list will remain as before. it won't add number in "numbers2" list
print(numbers2)


# numbers.clear()
# print(numbers)
