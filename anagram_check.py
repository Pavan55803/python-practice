# ============================================================
#                     ANAGRAM CHECK
# ============================================================

a = 'silent'
b = 'listen'

if sorted(a) == sorted(b):
    print(f"'{a}' and '{b}' are Anagrams")
else:
    print(f"'{a}' and '{b}' are Not Anagrams")
