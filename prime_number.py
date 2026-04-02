# ============================================================
#                   PRIME NUMBER CHECK
# ============================================================

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

test_numbers = [2, 7, 10, 13, 25, 37]
for n in test_numbers:
    result = "Prime" if is_prime(n) else "Not Prime"
    print(f"{n} --> {result}")
