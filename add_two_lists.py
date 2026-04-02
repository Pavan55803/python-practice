# ============================================================
#            ADD TWO LISTS ELEMENT BY ELEMENT
# ============================================================

l1 = [3, 4, 5]
l2 = [6, 7, 8]

# Method 1 - Using loop
res = []
for i in range(len(l1)):
    res.append(l1[i] + l2[i])
print("Using loop:", res)

# Method 2 - Using zip()
res2 = [a + b for a, b in zip(l1, l2)]
print("Using zip():", res2)
