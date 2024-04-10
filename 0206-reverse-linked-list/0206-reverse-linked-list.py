# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_func(node):
            if node == None or node.next == None:
                return node
            p = reverse_func(node.next)
            tmp = node.next
            tmp.next = node
            node.next = None
            return p
        return reverse_func(head)