# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack=[]
        temp=head
        while temp:
            stack.append(temp.val)
            temp=temp.next
        temp=head
        max_sum=0
        while temp:
            first=stack.pop()
            second=temp.val
            max_sum=max(max_sum,first+second)
            temp=temp.next
        return max_sum
            
        
        