class PageNode:
    def __init__(self, url: str, next=None, prev=None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = PageNode(homepage)
        self.tail = self.head
        self.current = self.head
              
    def visit(self, url: str) -> None:
        newPage = PageNode(url)
        self.current.next = newPage
        newPage.prev = self.current
        self.tail = newPage
        self.current = newPage

    def back(self, steps: int) -> str:
        i = 0
        while i < steps and self.current.prev != None:
            self.current = self.current.prev
            i+=1
        return self.current.url
    def forward(self, steps: int) -> str:
        i = 0
        while i < steps and self.current.next != None:
            self.current = self.current.next
            i+=1
        return self.current.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)