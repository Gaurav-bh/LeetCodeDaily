# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node):
            if node==None or node.next==None:
                return node
            a=node
            b=node.next
            a.next=helper(node.next.next)
            b.next=a
            return b
        return helper(head)

        