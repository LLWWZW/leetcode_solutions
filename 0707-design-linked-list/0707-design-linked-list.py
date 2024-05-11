class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.dump = ListNode(0)

    def get(self, index: int) -> int:
        if 0 <= index and index <= (self.size-1):
            head = self.dump
            for _ in range(index+1):
                head = head.next
            return head.val
        return -1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if 0 <= index and index <= (self.size):
            head = self.dump
            for _ in range(index):
                head = head.next
            tmp = head.next
            addATIndex_node = ListNode(val)
            head.next = addATIndex_node
            addATIndex_node.next = tmp
            self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if  0 <= index and index <= (self.size-1):
            head = self.dump
            for _ in range(index):
                head = head.next
            tmp = head.next
            head.next = tmp.next
            tmp.next = None
            self.size -= 1
        return 


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)