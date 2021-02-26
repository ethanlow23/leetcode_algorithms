# Valid Anagram

def isAnagram(s, t):
  if len(s) != len(t):
    return False
  count = [0] * 26
  for c in s:
    count[ord(c) - ord('a')] += 1
  for c in t:
    if count[ord(c) - ord('a')] == 0:
      return False
    else:
      count[ord(c) - ord('a')] -= 1
  return True
