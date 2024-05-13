# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dump = ListNode(0)
        dump.next = head
        slow , fast = dump, dump
        for _ in range(n):
            fast = fast.next
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dump.next