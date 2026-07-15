class ListNode:

    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        

class MyLinkedList:

    def __init__(self):
        #create dummy head and tail of vals 0
        self.head = ListNode()
        self.tail = ListNode()
        #link the dummy head to dummy tail
        self.head.next = self.tail
        #link dummy tail to prev head
        self.tail.prev = self.head
        #set size to 0
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size: return -1 #check if index out of range
        curr = self.head.next #start at head.next (after dummy head)

        #traverse until index
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size: return #check if index out of range
        curr = self.head.next #start at head.next (after dummy head)
        #traverse until index
        for _ in range(index):
            curr = curr.next
        #add ListNode at index
        newNode = ListNode(val) #create a node of val
        #create predeccesor and succesor pointers
        pred = curr.prev
        succ = curr
        #linking to predeccesor 
        newNode.prev = pred  #link newNode to pred
        pred.next = newNode #link pred to new node
        #linking to succesor 
        newNode.next =  succ #link newNode to succesor
        succ.prev = newNode #link the succesor to newNode
        self.size += 1 #update size

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size: return #check if index out of range
        curr = self.head.next #start at head.next (after dummy head)

        #traverse until index
        for _ in range(index):
            curr = curr.next
        #create predeccesor and succesor pointers
        pred = curr.prev
        succ = curr.next
        #d/c curr from pred and succ & link pred and succ to each other
        pred.next = succ
        succ.prev = pred
        self.size -= 1 #update size

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)