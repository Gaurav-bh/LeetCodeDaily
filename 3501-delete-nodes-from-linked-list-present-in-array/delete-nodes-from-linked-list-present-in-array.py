# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        prev = head
        while head.val in nums:
            prev = head
            head = head.next
        res = head
        if not head:
            return None

        while head.next:
            if head.next.val in nums:
                head.next = head.next.next
            else:
                head = head.next
        return res
        