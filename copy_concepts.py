# ============================================================
#              SHALLOW COPY vs DEEP COPY IN PYTHON
# ============================================================

import copy

# 1. Shallow Copy
# Changes to nested elements in original AFFECT the shallow copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
original[0][1] = 99

print("--- Shallow Copy ---")
print("Original:", original)
print("Shallow Copy:", shallow)  # Also changed!


# 2. Deep Copy
# Changes to original do NOT affect the deep copy
a = [['a', 'b'], ['c', 'd']]
deep = copy.deepcopy(a)
a[1][1] = 'z'

print("\n--- Deep Copy ---")
print("Original:", a)
print("Deep Copy:", deep)  # Unchanged


# Key Difference:
# Shallow Copy --> copies references (nested objects are shared)
# Deep Copy    --> copies everything (fully independent)
