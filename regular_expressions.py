# ============================================================
#                  REGULAR EXPRESSIONS IN PYTHON
# ============================================================

import re

# 1. Extract Digits from a String
text = 'I am in office, my id is 9876'
print("Digits:", re.findall(r'\d+', text))
print("Non-digits:", re.findall(r'\D+', text))
print("Words:", re.findall(r'\w+', text))
print("Spaces:", re.findall(r'\s', text))


# 2. Email Validation
def validate_email(email):
    pattern = r"^[a-zA-Z0-9]+[@][a-zA-Z]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        print(f"{email} --> Valid Email")
    else:
        print(f"{email} --> Invalid Email")

validate_email("pavan@gmail.com")
validate_email("pavan@.com")
validate_email("pavantest123@yahoo.com")


# 3. Mobile Number Validation (Indian Numbers starting with 8 or 9)
def validate_mobile(number):
    pattern = r"^[89][0-9]{9}$"
    if re.match(pattern, number):
        print(f"{number} --> Valid Mobile Number")
    else:
        print(f"{number} --> Invalid Mobile Number")

validate_mobile("9912305749")
validate_mobile("1234567890")
validate_mobile("8876543210")


# 4. Common Regex Patterns Reference
sample = 'I am in office , @ my id is 9876'
print("\n--- Regex Pattern Examples ---")
print("^ (starts with):", re.findall("^I am", sample))
print("$ (ends with):", re.findall("9876$", sample))
print(". (any char):", re.findall(r'i.', sample))
print("* (0 or more):", re.findall('o.*', sample))
print("+ (1 or more):", re.findall('i.+', sample))
print("? (0 or 1):", re.findall(r'o.?', sample))
