# The Fibonacci numbers are the numbers in the following integer sequence (Fn):

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

# such as

# F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
# test.assert_equals(productFib(4895), [55, 89, True])

def productFib(prod):
    a,b = 0,1
    while a*b<prod:
        a,b = b, a+b
    return [a,b,a*b==prod]
print(productFib(4895))
