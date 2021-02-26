# Palindrome Linked List

def isPalindrome(head):
    stack = []
    slow = fast = head
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
    while slow:
        if slow.val != stack.pop():
            return False
        slow = slow.next
    return True
