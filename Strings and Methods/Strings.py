name = "Harry"
city = 'Delhi'

message = """This is a
multi line
string"""

#Accessing Characters in a String
text = "Python"

print(text[0])
print(text[3])

#String Length
text = "Python"
length = len(text)

#String Slicing
text = "Python"
print(text[0:3])
print(text[2:])
print(text[:4])

text[-3:]     # same as text[6-3 : 6]
text[-5:-2]   # same as text[6-5 : 6-2]

# -3  ->  6 - 3 = 3
# -5  ->  6 - 5 = 1
# -2  ->  6 - 2 = 4


#Common String Methods

#lower() and upper()
text = "Python"
print(text.lower())
print(text.upper())

#strip()
text = "  hello  "
print(text.strip())

#replace()
text = "Hello World"
print(text.replace("World", "Python"))

#split()
text = "apple,banana,orange"
items = text.split(",")

#join()
items = ["apple", "banana", "orange"]
text = ",".join(items)

#find()
text = "Hello World"
position = text.find("World")

#startswith() and endswith()
email = "test@gmail.com"

print(email.startswith("test"))
print(email.endswith(".com"))

#String Concatenation
first = "Hello"
second = "World"

result = first + " " + second

#String Formatting
name = "Harry"
age = 25

message = f"My name is {name} and I am {age} years old"

#Checking String Content
text = "Python123"

print(text.isalpha())
print(text.isdigit())
print(text.isalnum())

#Strings are Immutable
text = "Python"
text[0] = "J"