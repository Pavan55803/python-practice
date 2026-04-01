# ============================================================
#                      FUNCTIONS IN PYTHON
# ============================================================

# 1. Basic Function with Parameters
def greet(name, age):
    print(name, age)

greet("Pavan", 23)


# 2. Function with *args - Filter Even Numbers
def even_numbers(*args):
    result = []
    for i in args:
        if i % 2 == 0:
            result.append(i)
    print("Even numbers:", result)

even_numbers(2, 3, 4, 5, 6, 8, 7, 9, 10)


# 3. Function with *args - Count Specific Letter
def count_letters(*args):
    a = list(args)
    print("Count of 'a':", a.count('a'))

count_letters('a', 'b', 'c', 'd', 'a', 'a')
