class Animal:
    def Speak(self):
        print("Speaking")

class Cat(Animal):
    language = "Meow"
    food = "Mouse"

    def CatDetails(self):
        print("Cat language: ", self.language)
        print("Cat food: ", self.food)

class Dog(Animal):
    language = "Bark"
    food = "Bones"

    def DogDetails(self):
        print("Dog language: ", self.language)
        print("Dog food: ", self.food)

dog = Dog()
dog.DogDetails()
dog.Speak()

cat = Cat()
cat.CatDetails()
cat.Speak()