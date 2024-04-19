income_dict = {
    "loan": '20000',
    "salary": '15000',
    "helb": '28000',
    "profit": '17899'

}
# set_income = True
# while set_income:
#     income = input("Enter income source(e.g Salary): ")
#     amount = input(f"Amount of income from {income}: ")
#     income_dict[income] = amount
#     add_income = input("Add another income source(Y/N): ").lower()
#     if add_income == "y":
#         pass
#     else:
#         print("exiting")
#         set_income = False
total_income = 0
for i in income_dict:
    print(income_dict[i])
    total_income += int(income_dict[i])
print(f"Total Income: {total_income}")

expenses_dict = {
    "rent": '3000',
    "water": '500',
    "internet": '1000',
    "shopping": '5000'
}
total_expenses = 0
for j in expenses_dict:
    print(expenses_dict[j])
    total_expenses += int(expenses_dict[j])
print(f"Total Expenses: {total_expenses}")
print(f"Balance is {total_income - total_expenses}")