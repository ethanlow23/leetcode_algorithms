# Binary Tree Level Order Traversal

from collections import deque

def levelOrder(root):
    # BFS
    res = []
    queue = deque()
    if root:
        queue.append(root)
    while queue:
        level = []
        for i in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level)
    return res
    # DFS
    res = []
    getLevelOrder(root, 0, res)
    return res

def getLevelOrder(root, level, res):
    if not root:
        return
    if level >= len(res):
        res.append([])
    res[level].append(root.val)
    getLevelOrder(root.left, level + 1, res)
    getLevelOrder(root.right, level + 1, res)
