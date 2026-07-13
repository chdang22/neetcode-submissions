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
            #this creates a list with val 0 at head
            #dummy stays pointing at head
            #node will move
            #the desired head of the merged list will be dummy.next to exclude the 0 val
        dummy = node = ListNode()
        #iterate through both lists
            #only move pointer through the list that has the lower value
        while list1 and list2: #while lists not null
            if list1.val < list2.val: #if list1 val is the lower
                node.next = list1 #first iteration, node.next is head. 
                    #add list1 curr to merge list 
                list1 = list1.next #move to next nnode in list1
            elif list1.val > list2.val:
                node.next = list2
                list2 = list2.next
            elif list1.val == list2.val:
                node.next = list1
                list1 = list1.next
            node = node.next #move to next node in merged list to prepare for next append

        if not list1 and list2: #if list1 is empty, append list 2(remaining nodes) to merged list
            node.next = list2
        elif not list2 and list1:
            node.next = list1
        
        return dummy.next  
        
