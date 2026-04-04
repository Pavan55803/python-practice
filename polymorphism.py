# ============================================================
#                  POLYMORPHISM IN PYTHON
# ============================================================
# Same method name, different behaviour based on the class

class A:
    def add(self):
        print("Method in Class A")

class B(A):
    def add(self):
        print("Method in Class B")

# Each class has its own version of add()
obj_a = A()
obj_a.add()  # Class A version

obj_b = B()
obj_b.add()  # Class B version

# -------------------------------------------------------

# Real world example of polymorphism
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self, r):
        return 3.14 * r * r

class Rectangle(Shape):
    def area(self, l, w):
        return l * w

c = Circle()
print("\nCircle area (r=5):", c.area(5))

r = Rectangle()
print("Rectangle area (4x6):", r.area(4, 6))
