# ============================================================
#               INHERITANCE & METHOD OVERRIDING
# ============================================================
# Child class overrides the parent class method
# This is called Method Overriding

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Child class method is called (overrides parent)
d = Dog()
d.speak()  # Dog barks

c = Cat()
c.speak()  # Cat meows

# Parent class method
a = Animal()
a.speak()  # Animal speaks
