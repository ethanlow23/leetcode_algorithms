# First Unique Character in a String

def firstUniqChar(s):
  count = {}
  for ch in s:
    if ch in count:
      count[ch] += 1
    else:
      count[ch] = 1
  for i in range(len(s)):
    if count[s[i]] == 1:
      return i
  return -1
