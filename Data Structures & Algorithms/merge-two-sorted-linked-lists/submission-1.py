# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #handle empty lists
        if not list1: return list2 #if list1 empty return list2 even if list 2 empty
        if not list2: return list1

        #create dummy list ptr and node ptr
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            elif list1.val > list2.val:
                node.next = list2
                list2 = list2.next
            elif list1.val == list2.val:
                node.next = list1
                list1 = list1.next
            node = node.next

        if not list1 and list2:
            node.next = list2
        elif not list2 and list1:
            node.next = list1
        
        return dummy.next  
        
