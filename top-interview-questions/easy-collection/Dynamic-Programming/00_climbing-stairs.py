# Climbing Stairs

def climbStairs(n):
  return getClimbStairs(n, {})

def getClimbStairs(n, memo):
  if n < 0:
    return 0
  if n == 1 or n == 2 or n == 3:
    return n
  if n in memo:
    return memo[n]
  else:
    memo[n] = getClimbStairs(n - 1, memo) + getClimbStairs(n - 2, memo)
    return memo[n]
