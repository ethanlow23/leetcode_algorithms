# 22. Generate Parentheses

def generateParentheses(n):
  ans = []
  getCombinations(n, 0, 0, "", ans)
  return ans

def getCombinations(n, left, right, cur, ans):
  if len(cur) == 2 * n:
    ans.append(cur)
  if (left < n):
    getCombinations(n, left + 1, right, cur + "(", ans)
  if (right < left):
    getCombinations(n, left, right + 1, cur + ")", ans)
