# House Robber

def rob(nums):
  if not nums:
    return 0
  if len(nums) == 1:
    return nums[-1]
  nums[1] = max(nums[1], nums[0])
  for i in range(2, len(nums)):
    nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
  return nums[-1]
