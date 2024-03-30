numbers = [6, 6, 5, 5, 5, 7, 4, 4, 7]
a = 0
for num in numbers:
    to_remove = numbers[a]
    if num == to_remove:
        numbers.remove(num)
        a += 1
print(numbers)

# how mosh did it
numbers = [6, 6, 5, 5, 5, 7, 4, 4, 7]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
