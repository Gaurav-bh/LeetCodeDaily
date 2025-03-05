# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ltr=True
        stack=[]
        rev=[]
        node=deque()
        next=deque()
        node.append(root)
        ans=[]
        if root==None:
            return ans
        while node:
            l=len(node)
            temp=[]
            print("node:- ",node)
            print()
            print()
            while l:
                curr=node.pop()
                temp.append(curr.val)
                if ltr:
                    if curr.left:
                        next.append(curr.left)
                    if curr.right:
                        next.append(curr.right)
                else:
                    if curr.right:
                        next.append(curr.right)
                    if curr.left:
                        next.append(curr.left)
                l-=1
            node=next
            next=[]
            ltr= not ltr
            ans.append(temp)
        return ans
            

        