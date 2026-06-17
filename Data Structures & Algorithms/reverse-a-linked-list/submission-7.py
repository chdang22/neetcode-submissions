# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head 
        prev = None
        while curr:
            temp = curr.next #save a temp ptr to next node before break link
            curr.next = prev #connect current node to prev (reverse the arrow)
            prev = curr #before move on, change make prev point to the current node (to connect the next node to this prev next iteration)
            curr = temp #move the current node to saved nnext one
        
        return prev #return the new head stored in prev (curr is null pointer now)