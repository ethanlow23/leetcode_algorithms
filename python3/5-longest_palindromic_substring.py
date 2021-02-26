# 5. Longest Palindromic Substring

def longestPalindrome(s):
  if not s or len(s) < 1:
    return ""
  start = 0
  end = 0
  for i in range(len(s)):
    len1 = getLongestPalindrome(s, i, i)
    len2 = getLongestPalindrome(s, i, i + 1)
    longer = max(len1, len2)
    if longer > end - start:
      start = i - (longer - 1) // 2
      end = i + longer // 2
  return s[start:end + 1]
    

def getLongestPalindrome(s, c1, c2):
  while c1 >= 0 and c2 < len(s) and s[c1] == s[c2]:
    c1 -= 1
    c2 += 1
  return c2 - c1 - 1
