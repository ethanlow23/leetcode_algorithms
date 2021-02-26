# 46. Permutations

def permute(nums):
  ans = []
  getPermutations(nums, [], ans)
  return ans

def getPermutations(nums, cur, ans):
  if not nums:
    ans.append(cur)
    return
  for i in range(len(nums)):
    getPermutations(nums[:i] + nums[i+1:], cur + [nums[i]], ans)
