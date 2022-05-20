from math import sqrt

def is_prime(num):
    if num<=1:
        return False
    count = 2
    while count<=sqrt(num):
        if num%count == 0:
            return False
        count += 1
    return True
print(is_prime(15))