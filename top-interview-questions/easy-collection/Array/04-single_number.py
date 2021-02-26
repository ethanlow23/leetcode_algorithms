# Single Number

def singleNumber(nums):
  count = {}
  for n in nums:
    if n not in count:
      count[n] = 1
    else:
      count[n] += 1
  for key in count:
    if count[key] == 1:
      return key
