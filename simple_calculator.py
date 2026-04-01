# ============================================================
#                     SIMPLE CALCULATOR
# ============================================================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def calculator():
    print("=" * 40)
    print("          Simple Calculator")
    print("=" * 40)
    print("Operations: + | - | * | /")

    while True:
        try:
            a = float(input("\nEnter first number: "))
            op = input("Enter operation (+, -, *, /): ")
            b = float(input("Enter second number: "))

            if op == '+':
                print(f"Result: {a} + {b} = {add(a, b)}")
            elif op == '-':
                print(f"Result: {a} - {b} = {subtract(a, b)}")
            elif op == '*':
                print(f"Result: {a} * {b} = {multiply(a, b)}")
            elif op == '/':
                print(f"Result: {a} / {b} = {divide(a, b)}")
            else:
                print("Invalid operation. Please use +, -, *, /")

            again = input("\nCalculate again? (yes/no): ").lower()
            if again != 'yes':
                print("Thank you for using the calculator!")
                break

        except ValueError:
            print("Error: Please enter valid numbers.")

calculator()
