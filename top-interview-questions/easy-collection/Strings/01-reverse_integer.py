# Reverse Integer

def reverse(x):
    ans = 0
    n = abs(x)
    while n:
        ans = ans * 10 + (n % 10)
        n //= 10
    if x < 0:
        return -ans
    else:
        return ans
