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
print("Intersection", intersection)