# fruits = ["apple", "banana", "lemon"]
#
# for fruit in fruits:  # for i in fruits
#     print(fruit + " " + "pie")  # print(i) -- gives same output

# for num in range(3, 100): # you can make it range(3,100,3)
#     if num % 3 == 0:
#         print(num)

## fizz buzz challenge
# if a number is divisible by 3 print fizz
# if a number is divisible by 5 print buzz
# if a number is divisible by both print fizzbuzz

for num in range(1, 100):
    if num % 3 == 0:
        if num % 5 == 0:
            print(str(num) + "fizzbuzz")
        else:
            print(str(num) +"fizz")
    elif num % 5 == 0:
        print(str(num) + "buzz")
    else:
        print("SKIP")