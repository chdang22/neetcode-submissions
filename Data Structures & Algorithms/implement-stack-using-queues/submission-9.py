class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self,val):
        newNode = ListNode(val)
        #Is not empty
        if self.tail:
            self.tail.next = newNode
        else:
            self.head = newNode
        self.tail = newNode
        self.size += 1
    def empty(self):
        return self.size == 0

    def dequeue(self)->int:
        #if empty
        if not self.head: raise IndexError("empty")
        #get val
        val = self.head.val
        #set new head to "remove" the curr node
        self.head = self.head.next
        if not self.head: 
            self.tail = None #list now empty, set tail to none

        self.size -= 1
        return val

class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.use_q1 = True

    def push(self, x: int) -> None:
        if self.use_q1:
            self.q1.enqueue(x)
        else:
            self.q2.enqueue(x)

    def pop(self) -> int:
        active = self.q1 if self.use_q1 else self.q2
        inactive = self.q2 if self.use_q1 else self.q1
    
        while active.size > 1:
            inactive.enqueue(active.dequeue())
        top_val = active.dequeue()
        self.use_q1 = not self.use_q1 #switch the flag
        return top_val #simulate pop
    def top(self) -> int:

        active = self.q1 if self.use_q1 else self.q2
        inactive = self.q2 if self.use_q1 else self.q1
        while active.size > 1:
            inactive.enqueue(active.dequeue())
        top_val = active.dequeue()
        inactive.enqueue(top_val)
        self.use_q1 = not self.use_q1
        return top_val
    def empty(self) -> bool:
        if self.q1.empty() and self.q2.empty():
            return True
        else: return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()