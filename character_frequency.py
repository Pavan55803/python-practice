# ============================================================
#           CHARACTER FREQUENCY USING COUNTER
# ============================================================

from collections import Counter

text = 'pawankalyan'
count = Counter(text)

print(f"Character frequency in '{text}':")
for char, freq in count.items():
    print(f"  {char} = {freq}")
