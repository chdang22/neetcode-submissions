class ListNode:
    #for use in MyLinkedList class
    def __init__(self, val=0, next= None, prev =None):
        self.val = val #make node of default val 0 or given param val
        self.next = next #set next to none
        self.prev = prev #set prev to none
     

class MyLinkedList:

    def __init__(self):
        #set dummy nodes to avoid empty list cases
        #insertion wioll happen b/w head and head.next
        self.head = ListNode(0) #dummy head 
        self.tail = ListNode(0) #dummy tail
        self.head.next = self.tail #for inserting between head and head.next
        self.tail.prev = self.head
        self.size = 0 #tracks real nodes in list, can check if i is out of bounds without traversal

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        
        succ = self.head
        for _ in range(index):
            succ = succ.next
        
        pred = succ
        succ = succ.next
        
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add
            

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        pred = self.head
        for _ in range(index):
            pred = pred.next
        
        succ = pred.next.next
        
        self.size -= 1
        pred.next = succ
        succ.prev = pred