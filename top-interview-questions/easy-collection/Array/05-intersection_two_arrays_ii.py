# Intersection of Two Arrays II

def intersect(nums1, nums2):
  res = []
  count = {}
  for n in nums1:
    if n in count:
      count[n] += 1
    else:
      count[n] = 1
  for n in nums2:
    if n in count and count[n] > 0:
      res.append(n)
      count[n] -= 1
  return res
