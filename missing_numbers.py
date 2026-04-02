# ============================================================
#            FIND MISSING NUMBERS IN A LIST
# ============================================================

num = [1, 3, 4, 5, 6, 8]
start = min(num)
stop = max(num)

print("Original list:", num)
print("Missing numbers:", end=" ")
for i in range(start, stop + 1):
    if i not in num:
        print(i, end=" ")
print()
