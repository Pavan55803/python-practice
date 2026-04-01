# ============================================================
#                    MISCELLANEOUS PROGRAMS
# ============================================================

# 1. Factorial of a Number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Factorial of 5:", factorial(5))
print("Factorial of 6:", factorial(6))


# 2. FizzBuzz Variation (Pavan, Murali, Syed)
def custom_fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('Syed')
        elif i % 3 == 0:
            print('Pavan')
        elif i % 5 == 0:
            print('Murali')
        else:
            print(i)

print("\n--- Custom FizzBuzz (1 to 15) ---")
custom_fizzbuzz(15)


# 3. Find Largest of Three Numbers
def find_largest(a, b, c):
    if a >= b and a >= c:
        return f"{a} is the largest"
    elif b >= c:
        return f"{b} is the largest"
    else:
        return f"{c} is the largest"

print("\n--- Largest Number ---")
print(find_largest(10, 25, 17))
