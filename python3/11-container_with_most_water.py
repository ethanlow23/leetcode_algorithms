# 11. Container With Most Water

def maxArea(height):
  water = 0
  left, right = 0, len(height) - 1
  while left < right:
    cur = min(height[left], height[right]) * (right - left)
    water = max(water, cur)
    if height[left] < height[right]:
      left += 1
    else:
      right -= 1
  return water
