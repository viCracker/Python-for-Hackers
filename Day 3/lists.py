# distro = ["Debian", "Uvuntu", "Kali", "Mint", "Arch"]
# distro[1] = "Ubuntu"
# print(distro[-2])  # print the second last item
# print(distro[0:4])  # print list from index zero to 4 excluding the value at 4

numbers = [1, 2, 3, 4, 5]
numbers.append(6)   # adds an item at the end
numbers.insert(6, 7)   #adds an item(7) at index 6
numbers.remove(3)   #removes 3 from the list to remove everything use numbers.clear()

print(numbers)
print(1 in numbers)     #check if 1 is in the list
print(len(numbers))     #check number of items in list
