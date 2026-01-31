student = {
    "name": "Gayu",
    "city": "BBSR",
    "comapny": "Microsoft"
}

student.pop("name")
print(student)

student["class"] = "12th"
print(student)
student.popitem()
print(student)

del student['city']