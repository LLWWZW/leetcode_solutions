# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dump = ListNode(0)
        dump.next = head
        prev = dump
        move = head
        while move and move.next:
            tmp = move.next
            move.next = tmp.next
            tmp.next = move
            prev.next = tmp

            prev = move
            move = move.next
        return dump.next