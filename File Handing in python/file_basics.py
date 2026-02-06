a = "Gunu is beautiful"

# file = open("gunu.txt", "w")
# file.write(a)

file = open("robot.txt", "r")
content = file.read()
print(content)

file.close()