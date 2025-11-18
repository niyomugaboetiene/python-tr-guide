students = {'alice': 80, 'erice': 100}

# ascending
ascending = list(sorted(students.items()))
descending = list(sorted(students.items(), reverse=True))
print("ascending dictionary", ascending)
print("descending dictionary", descending)