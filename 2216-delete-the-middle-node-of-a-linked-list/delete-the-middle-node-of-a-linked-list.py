# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s,f=head,head
        if f ==None or f.next==None :
            return head.next 
        f=f.next.next
        while f and f.next:
            s=s.next
            f=f.next.next
        s.next=s.next.next
        return head 


        
        

        