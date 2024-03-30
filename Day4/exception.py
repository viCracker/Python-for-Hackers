try:
    age = int(input("Age: "))
    income = 2000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be o")
except ValueError:
    print("Invalid Value")
