# 94. Binary Tree Inorder Traversal

def inorderTraversal(root):
"""
  # RECURSIVE
  order = []
  getInorderTraversal(root, order)
  return order
"""
  # ITERATIVE
  order = []
  stack = []
  cur = root
  while cur or stack:
    while cur:
      stack.append(cur)
      cur = cur.left
    cur = stack.pop()
    order.append(cur.val)
    cur = cur.right
  return order

def getInorderTraversal(root, res):
  if root:
    getInorderTraversal(root.left, res)
    res.append(root.val)
    getInorderTraversal(root.right, res)
