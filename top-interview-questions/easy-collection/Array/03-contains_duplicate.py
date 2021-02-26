# Contains Duplicate

def containsDuplicate(nums):
  elements = set()
  for n in nums:
    if n in elements:
      return True
    elements.add(n)
  return False
