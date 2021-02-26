# 24. Swap Nodes in Pairs

def swapPairs(head):
  dummy = ListNode(0)
  dummy.next = head
  cur = dummy
  while cur.next and cur.next.next:
    slow = cur.next
    fast = cur.next.next
    cur.next = fast
    slow.next = fast.next
    fast.next = slow
    cur = cur.next.next
  return dummy.next
