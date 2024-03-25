# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers
# numbers = int(input("How many numbers do want to enter: \n"))
# for i in range (numbers):
#     num = int(input("Enter numbers separating by comma:\n"))
#     print(list(num))
#     print(tuple(num))

numbers = input("Please enter numbers: \n")
list = numbers.split(":")
tuple = tuple(list)
print("List: ", list)
print("Tuple: ", tuple)