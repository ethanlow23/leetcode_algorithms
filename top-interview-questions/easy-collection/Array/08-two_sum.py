# Two Sum

def twoSum(nums, target):
  seen = {}
  for i in range(len(nums)):
    rem = target - nums[i]
    if rem in seen:
      return [seen[rem], i]
    else:
      seen[nums[i]] = i
  return [-1, -1]
