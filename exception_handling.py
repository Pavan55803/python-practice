# ============================================================
#                  EXCEPTION HANDLING IN PYTHON
# ============================================================

# 1. Division with ZeroDivisionError and ValueError Handling
def safe_divide():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a / b)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter a valid number.")
    finally:
        print("Thank you!")

safe_divide()


# 2. Filter Even Numbers from a List with Exception Handling
def filter_even(numbers):
    result = []
    try:
        for i in numbers:
            if i % 2 == 0:
                result.append(i)
        print("Even numbers:", result)
    except Exception as e:
        print("Error:", e)
    finally:
        print("Successfully executed.")

filter_even([1, 2, 4, 3])
