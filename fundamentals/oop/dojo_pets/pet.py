class Pet:
    # implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks = []):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 0
        self.energy = 0
    
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        return self

    # noise() - prints out the pet's sound
    def noise(self):
        print("Bark!")
        return self

# Sub class of Pet: Cat
class Cat(Pet):
    def __init__(self, name, type, tricks=[]):
        super().__init__(name, type, tricks)
    
    # noise() - prints out the pet's sound
    def noise(self):
        print("Meow!")
        return self
