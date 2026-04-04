# ============================================================
#                  GENERATORS IN PYTHON
# ============================================================
# Generator uses 'yield' instead of 'return'
# It generates values one at a time - saves memory

def square_generator(n):
    for i in range(1, n + 1):
        yield i * i

print("Squares using generator:")
for num in square_generator(5):
    print(num, end=" ")
print()

# -------------------------------------------------------

# Another example - even number generator
def even_generator(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i

print("\nEven numbers using generator:")
for num in even_generator(10):
    print(num, end=" ")
print()
