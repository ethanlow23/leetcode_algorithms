# 75. Sort Colors

def sortColors(nums):
  red = white = blue = 0
  for n in nums:
    if n == 0:
      red += 1
    elif n == 1:
      white += 1
    else:
      blue += 1
  for i in range(len(nums)):
    if i < red:
      nums[i] = 0
    elif i < red + white:
      nums[i] = 1
    else:
      nums[i] = 2
  return
