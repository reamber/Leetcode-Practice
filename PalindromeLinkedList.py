# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slowPoint = head
        fastPoint = head
        
        firstHalf = []
        secondHalf = []
        
        while slowPoint:
            if fastPoint:
                firstHalf.append(slowPoint.val)
                fastPoint = fastPoint.next
                if fastPoint:
                    fastPoint = fastPoint.next
            else:
                secondHalf.append(slowPoint.val)
            slowPoint = slowPoint.next
        
        if len(firstHalf) != len(secondHalf):
            return firstHalf[:-1] == secondHalf[::-1]
        return firstHalf == secondHalf[::-1]
            
            
        
