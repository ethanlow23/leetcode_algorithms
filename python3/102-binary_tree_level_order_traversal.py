# 102. Binary Tree Level Order Traversal

def levelOrder(root):
"""
  # RECURSIVE
  res = []
  getLevelOrder(root, 0, res)
  return res
"""
  # ITERATIVE
  res = []
  if not root:
    return res
  stack = [root]
  while stack:
    values = []
    parents = stack
    stack = []
    for parent in parents:
      values.append(parent.val)
      if parent.left:
        stack.append(parent.left)
      if parent.right:
        stack.append(parent.right)
    res.append(values)
  return res

def getLevelOrder(root, level, res):
  if not root:
    return
  if level > len(res) - 1:
    res.append([])
  res[level].append(root.val)
  getLevelOrder(root.left, level + 1, res)
  getLevelOrder(root.right, level + 1, res)
