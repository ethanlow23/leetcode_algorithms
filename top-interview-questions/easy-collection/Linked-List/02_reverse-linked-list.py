# Reverse Linked List

def reverseList(head):
    # ITERATIVE
    prev = None
    curr = head
    while curr.next:
        prev = curr.next
        curr.next = prev.next
        prev.next = head
        head = prev
    return head
    # RECURSIVE
    if not head or not head.next:
        return head
    node = reverseList(head.next)
    head.next.next = head
    head.next = None
    return node
