# ============================================================
#                    LIST OPERATIONS IN PYTHON
# ============================================================

# 1. Separate Unique and Duplicate Values
a = [1, 2, 2, 3, 3, 4, 5]

unique = []
duplicates = []
for i in a:
    if a.count(i) < 2:
        unique.append(i)
    else:
        duplicates.append(i)

print("Unique values:", unique)
print("Duplicate values:", list(set(duplicates)))


# 2. Separate Strings and Integers from a Mixed List
mixed = ['a', 'b', 'c', 1, 2, 3]
strings = []
integers = []

for i in mixed:
    if type(i) == str:
        strings.append(i)
    else:
        integers.append(i)

print("Strings:", strings)
print("Integers:", integers)


# 3. Sum of Even, Odd, and Total Numbers
numbers = [1, 2, 3, 4, 5, 6]
total = 0
even_sum = 0
odd_sum = 0

for i in numbers:
    total += i
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
print("Total sum:", total)


# 4. Find Maximum Value Without Built-in max()
a = [5, 6, 45, 78, 6]
max_val = 0
for i in a:
    if i > max_val:
        max_val = i
print("Maximum value:", max_val)


# 5. Slice a List
a = ['abc', 'cba', 'daf', 'fed']
print("First half:", a[0:2])
print("Second half:", a[2:4])
