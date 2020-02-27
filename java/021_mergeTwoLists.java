class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode newList = new ListNode(0);
        ListNode runner = newList;
        while (l1 && l2) {
            if (l1.val <= l2.val) {
                runner.next = l1;
                l1 = l1.next;
            } else {
                runner.next = l2;
                l2 = l2.next;
            }
            runner = runner.next;
        }
        runner.next = l1 ? l1 : l2;
        return newList.next;
    }
}