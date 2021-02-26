# Remove Duplicates from Sorted Array

def removeDuplicates(nums):
  curr = 0
  for i in range(len(nums)):
    if nums[i] != nums[curr]:
      curr += 1
      nums[curr] = nums[i]
  return curr + 1
