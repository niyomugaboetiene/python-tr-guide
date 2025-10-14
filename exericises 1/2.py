fruits = ["Apple", "Banana", "Chery", "Orange"]

fruits.append("Mango")
fruits.remove("Banana")
index = fruits.index("Orange")
fruits[index] = "Grape"

for fruit in fruits:
    print(fruit)