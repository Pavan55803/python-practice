# ============================================================
#                  STRING MANIPULATION IN PYTHON
# ============================================================

# 1. Reverse a String Using Slicing
name = 'pavan'
print("Reversed (slicing):", name[::-1])


# 2. Reverse a String Without Slicing
name = 'pavan'
reversed_name = ''
for i in name:
    reversed_name = i + reversed_name
print("Reversed (loop):", reversed_name)


# 3. Check if a String is a Palindrome
def is_palindrome(s):
    return s == s[::-1]

print("madam is palindrome:", is_palindrome("madam"))
print("hello is palindrome:", is_palindrome("hello"))


# 4. Count a Specific Word in a Sentence
sentence = "I am working in level 5 org in my org"
count = 0
words = sentence.split()
for word in words:
    if word == 'org':
        count += 1
print("Count of 'org':", count)


# 5. Run-Length Encoding (Count Consecutive Characters)
a = 'aaabbbcc'
result = ''
count = 1
for i in range(1, len(a)):
    if a[i] == a[i - 1]:
        count += 1
    else:
        result += f"{count}{a[i-1]}"
        count = 1
result += f"{count}{a[-1]}"
print("Run-length encoding of 'aaabbbcc':", result)


# 6. Sum of Digits of Each Number in a List
numbers = [333, 222]
for num in numbers:
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num //= 10
    print("Sum of digits:", total)
