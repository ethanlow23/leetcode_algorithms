# Symmetric Tree

from collections import deque

def isSymmetric(root):
    # ITERVATIVE
    queue = deque([root, root])
    while queue:
        t1 = queue.popleft()
        t2 = queue.popleft()
        if not t1 and not t2:
            continue
        if not t1 or not t2 or t1.val != t2.val:
            return False
        queue.append(t1.left)
        queue.append(t2.right)
        queue.append(t1.right)
        queue.append(t2.left)
    return True
    # RECURSIVE
    return checkSymmetry(root, root)

def checkSymmetry(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2 or t1.val != t2.val:
        return False
    return checkSymmetry(t1.left, t2.right) and checkSymmetry(t1.right, t2.left)
