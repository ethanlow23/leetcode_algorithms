# Validate Binary Search Tree

def isValidBST(root):
    return checkBST(root, float('-inf'), float('inf'))

def checkBST(root, mn, mx):
    if not root:
        return True
    elif root.val <= mn or root.val >= mx:
        return False
    else:
        return checkBST(root.left, mn, root.val) and checkBST(root.right, root.val, mx)
