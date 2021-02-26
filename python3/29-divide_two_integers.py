# 29. Divide Two Integers

# TIME LIMIT EXCEEDED
def divide(dividend, divisor):
  x = abs(dividend)
  y = abs(divisor)
  ans = 0
  while x >= y:
    x -= y
    ans += 1
  if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
    return ans
  else:
    return -ans
