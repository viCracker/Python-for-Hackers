# Write a program to find the largest number in a list
numbers = [1, 2, 4, 60, 6]
max = numbers[0] # sets largest number to 1(numbers[0])
for num in numbers:
    if num >= max:
        max = num   # sets any number larger than 1, to largest number
print(f"largest number is: {max}")
