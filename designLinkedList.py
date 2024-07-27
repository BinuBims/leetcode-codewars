class ListNode:
    def __init__(self,val):
        self.val =  val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and cur != self.right and index == 0:
            return cur.val
        return -1
        
    def addAtHead(self, val: int) -> None:
        head,next,prev = ListNode(val), self.left.next, self.left
        head.next = next
        head.prev = prev
        next.prev = head
        prev.next = head
        

    def addAtTail(self, val: int) -> None:
        tail,nex,prev = ListNode(val), self.right, self.right.prev
        tail.next = nex
        tail.prev = prev
        nex.prev = tail
        prev.next = tail

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        

        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and index == 0:
            new,nxt,prev = ListNode(val), cur, cur.prev
            new.next = nxt
            new.prev = prev
            prev.next = new
            nxt.prev = new

        

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and cur != self.right and index == 0:
            nxt,prev = cur.next, cur.prev
            nxt.prev = prev
            prev.next = nxt