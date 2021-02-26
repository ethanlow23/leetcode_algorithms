# Convert Sorted Array to Binary Search Tree

def sortedArrayToBST(nums):
    return constructBST(nums, 0, len(nums) - 1)

def constructBST(nums, left, right):
    if left == right:
        return TreeNode(nums[left])
    if left < right:
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = constructBST(nums, left, mid - 1)
        node.right =constructBST(nums, mid + 1, right)
        return node
