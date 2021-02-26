# 3. Longest Substring Without Repeating Characters

def lengthOfLongestSubstring(s):
  longest = slow = 0
  characters = {}
  for i, ch in enumerate(s):
    if ch in characters and slow <= characters[ch]:
      slow = characters[ch] + 1
    else:
      longest = max(longest, i - slow + 1)
    characters[ch] = i
  return longest
