# ============================================================
#         FIND SECOND LARGEST NUMBER USING REGEX
# ============================================================

import re

a = [1, 4, 3, 5, 5, 'a,b']

# Convert list to string and extract all numbers using regex
num = str(a)
num = re.findall(r'\d+', num)

# Remove duplicates and sort
b = list(set(num))
b.sort(key=lambda x: int(x))  # Sort as integers not strings

print("Numbers found:", b)

if len(b) > 1:
    second_largest = b[-2]
    print("Second largest:", second_largest)
