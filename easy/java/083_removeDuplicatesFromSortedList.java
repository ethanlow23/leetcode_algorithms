class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) return head;
        ListNode runner = head;
        while (runner.next != null) {
            if (runner.val == runner.next.val) {
                runner.next = runner.next.next;
            } else {
                runner = runner.next;
            }
        }
        return head;
    }
}