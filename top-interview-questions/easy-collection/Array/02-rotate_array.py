# Rotate Array

def rotate(nums, k):
  k = k % len(nums)
  nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
