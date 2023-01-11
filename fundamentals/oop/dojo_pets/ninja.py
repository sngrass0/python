from pet import Pet, Cat

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        print(f"{self.first_name} took {self.pet.name} on a walk!!")
        return self

    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            self.pet.eat()
            print(f"{self.first_name} fed {self.pet.name} {food}!!")
        else:
            print(f"Oh No! There's no more food to feed {self.pet.name}")
        return self

    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()
        return self

# Implementing Classes
dog_treats = ["Bone", "Greenie"]
cat_treats = ["Frisky", "Greenie"]
blossoms_food = ["Chicken", "Kibble", "Steak"]
eowyns_food = ["Chicken", "Kibble", "Steak"]

Steph = Ninja("Stephanie", "Grasso", dog_treats, blossoms_food, Pet("Blossom", "dog", ["sit", "roll over"]))
Steph.walk().feed().bathe().bathe().feed().feed().feed()

Rosie = Ninja("Rosie", "Zywicki", cat_treats, eowyns_food, Cat("Eowyn", "cat"))
Rosie.feed().feed().bathe()


