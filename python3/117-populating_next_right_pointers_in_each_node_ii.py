# 117. Populating Next Right Pointers in Each Node II

def connect(root):
  dummy = runner = Node(0)
  while root:
    runner.next = root.left
    if runner.next:
      runner = runner.next
    runner.next = root.right
    if runner.next:
      runner = runner.next
    node = node.next
    if not node:
      runner = dummy
      node = dummy.next
