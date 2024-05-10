# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dump = ListNode()
        dump.next = head
        slow = dump
        fast = head
        while fast is not None:
            if fast.val != val:
                slow.next = fast
                slow = fast
            fast = fast.next
            if fast is None:
                slow.next = None

        return dump.next