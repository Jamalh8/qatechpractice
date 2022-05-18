from abc import ABC, abstractmethod

# We are going to create some classes. The superclass is going to be Bird.
class Bird(ABC):
    fly = True
    babies = 0

    def noise(self):
        return "Squawk"

    def reproduce(self):
        self.babies += 1

    @abstractmethod
    def eat(self):
        pass

    extinct = False


# Now we are going to create the first subclass.
class Owl(Bird):

    def reproduce(self):
        self.babies += 6

    def eat(self):
        return "Peck peck"


# Now we will add another subclass.
class Dodo(Bird):
    Fly = False
    extinct = True

    def eat(self):
        return "Nom nom"

    def reproduce(self):
        if not self.extinct:
            self.babies += 1

dodo1= Dodo()
owl1= Owl()

owl1.reproduce()
print(owl1.babies)
dodo1.reproduce()
print(dodo1.babies)

print(owl1.eat())
print(dodo1.eat())
print(owl1.noise())
print(dodo1.noise())

