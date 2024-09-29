class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        raise NotImplementedError("This method should be overridden in subclasses.")

class Cow(Animal):
    def make_sound(self):
        return "moo"

class Dog(Animal):
    def make_sound(self):
        return "woof"

class Cat(Animal):
    def make_sound(self):
        return "meow"

class Pig(Animal):
    def make_sound(self):
        return "oink"

class Duck(Animal):
    def make_sound(self):
        return "quack"

class Horse(Animal):
    def make_sound(self):
        return "neigh"

class Sheep(Animal):
    def make_sound(self):
        return "baa"

class Chicken(Animal):
    def make_sound(self):
        return "cluck"

class Goat(Animal):
    def make_sound(self):
        return "bleat"

class Frog(Animal):
    def make_sound(self):
        return "ribbit"
