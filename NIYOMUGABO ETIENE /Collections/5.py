# Create a dictionary of student data (name, age,sex, adress course, class ) and print keys/values.

Student = {
    "name": "Etiene", "age": 12, "sex": "male", "address": "Rwanda", "course": "Python programming", "class": "L5SOD",
}

print("Student Details", Student)
print(Student["sex"])

# Update, add, and delete dictionary items.

# update
newAge = Student["age"] = 18
print(newAge)

# add
NewDetail = Student["district"] = "Bugesera"

# delete
del Student
