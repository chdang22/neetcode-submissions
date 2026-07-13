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

        #create dummy list ptr and tail ptr
            # this creates a list with val 0 at head
            # dummy stays pointing at head
            # tail will move
            # the desired head of the merged list will be dummy.next to exclude the 0 val
        dummy = tail = ListNode() # essentially head = tail
        
        # iterate through both lists   
        while list1 and list2:
            if list1.val <= list2.val: # if val1 smallest or equal
                tail.next = list1 # append list1 curr to merged list tail
                list1 = list1.next  # if equal, either list can next, list1 is chosen arbitrarily 
            else: # otherwise val2 is smallest
                tail.next = list2
                list2 = list2.next
            tail = tail.next #advance tail to null spot
        #append whichever list remains to merged list
        tail.next = list1 or list2
        
        return dummy.next  
        
