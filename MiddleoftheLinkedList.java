/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
// pointer -> this.next
// pointer -> this.next.next 2x speed

// 1 -> 2 -> 3
// 1 -> 2 -> 3 -> 4 -> 5
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode first = new ListNode(); //next
        ListNode second = new ListNode(); //next.next 2x speed
        first = head;
        second = head;
        Boolean isNext = true;
        while(isNext){//check if it reaches the tail
            if (second.next == null) {
                isNext = false;
            }
            else {
                first = first.next;
                if(second.next.next == null){
                    isNext = false;
                }
                else {
                    second = second.next.next;
                }
            }

        }
        
        return first;
    }
}
