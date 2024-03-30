#to generate F
numbers = [5,2,5,2,2]
print("Method 1: Beginner")
for number in numbers:
    print(number * "b")
print("Method 2: Intermediate")
for num in numbers:
    if num == 5:
        print("iiiii")
    else:
        print("ii")
print("Method 3: Advanced") #mosh used
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'a'
    print(output)