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

    def peek(self) -> int:
        if not self.head: raise IndexError("empty")
        val = self.head.val
        return val
    
    def isEmpty(self)->bool:
        return self.size == 0
        
        
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = Queue() #students
        q2 = Queue() #sandwiches
        cycled = 0
        for s in students:
            q.enqueue(s)
        for s in sandwiches:
            q2.enqueue(s)
        while cycled<q.size:
            stud = q.peek()
            sand = q2.peek()
            if stud == sand:
                q2.dequeue() #remove sandwich
                q.dequeue() #remove students
                cycled = 0
            elif stud != sand:
                sad_student = q.dequeue() #remmove student and store in sad_student
                q.enqueue(sad_student) #add sad_student to end of q
                cycled +=1
        return q.size
            

