# ============================================================
#           DEFAULT ARGUMENTS IN CLASS METHODS
# ============================================================

class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()

print("Add two numbers (1+2):", calc.add(1, 2))      # c defaults to 0
print("Add three numbers (1+2+3):", calc.add(1, 2, 3))  # c = 3
