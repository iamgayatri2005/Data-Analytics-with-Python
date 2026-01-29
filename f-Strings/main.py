name = input("Whats your name: ")
work = input("Where do you work: ")
live = input("Where do you live?: ")

# Harry works at CodeWithHarry and lives in Delhi
# print(name + " works at " + work + " and lives in " + live) 👎

#👉 Here, {name} and {age} are automatically replaced with their actual values.
print(f"{name} works at {work} and lives in {live}")