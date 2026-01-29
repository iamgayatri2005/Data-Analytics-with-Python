# print("Hey this is my program")

# age = int(input("Enter your age: "))

# print(age + 10)

# price = float(input())
# print("The price is ", price)

#The input() function pauses the program and waits for the user to type something.
name = input()

#You can guide the user by showing a message inside input().
name = input("Enter your name: ")

#Even if the user enters a number, Python will treat it as text.
age = input("Enter your age: ")
type(age)

#If you want to perform calculations, you must convert the input.
age = int(input("Enter your age: "))

#For decimal values, use float().
price = float(input("Enter product price: "))

#Using User Input in Calculations
quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))

total = quantity * price
print("Total amount:", total)

#Common Input Errors
age = int(input("Enter age: "))