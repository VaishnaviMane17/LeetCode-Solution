# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head
        curr = None
        while fast and fast.next:
            curr = slow
            slow = slow.next
            fast = fast.next.next

        if not curr:
            return None
        if curr:
            curr.next = slow.next    
        # slow.next = None

        return head


        
        

        