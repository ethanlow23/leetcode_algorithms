# 49. Group Anagrams

import collections

def groupAnagrams(strs):
  ans = collections.defaultdict(list)
  for word in strs:
    key = sorted(word)
    ans[tuple(key)].append(word)
  return ans.values()
