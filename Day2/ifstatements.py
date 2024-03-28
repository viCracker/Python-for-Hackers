# fnum = input("First Number: ")
# snum = input("Second Number: ")

# if fnum > snum:
#     lnum = fnum #large number, smallnumber
#     smnum = snum
# else:
#     lnum = snum
#     smnum = fnum
# print(f"{lnum} is greater than {smnum}")

# if fnum > snum:
#     print("The first is larger")
# elif snum > fnum:
#     print("The second is larger")
# else:
#     print("They equal")

# Program for Grading using if

score = int(input("Enter Your Score"))
if score >= 89:  # 89 <= score <= 100
    age= int(input("Your Age:"))
    if age < 15:
        print("You got A+")
    else:
        print("Your grade is A")
elif 78 <= score:
    print("Grade B")
elif 68 <= score:
    print("Grade C")
elif 58 <= score <= 67:
    print("Grade D")
elif 0 <= score <= 57:
    print("Grade F")
else:
    print("Error")

