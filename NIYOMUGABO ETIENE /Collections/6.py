# Create two sets and perform union, intersection, and difference.
num1 = { 1, 2, 4, 4, 5 }
num2 = { 1, 2, 6, 7, 9 }

combination = num1.union(num2)
# methood 2
comb = num1 | num2

print("Combined ", comb)
print("Combined ", combination)

# intersection
intersection = num1.intersection(num2)

# methood 2
intersect = num1 & num2
print("Intersection", intersect)
print("Intersection", intersection)

# difference
difference = num1.difference(num2)
print("DIfference", difference)