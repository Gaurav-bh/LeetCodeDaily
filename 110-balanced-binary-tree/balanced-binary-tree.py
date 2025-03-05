# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root==None:
                return (0,True)
            l=height(root.left)
            r=height(root.right)
            if abs(l[0]-r[0])<=1 and l[1] and r[1]:
                return ((max(l[0],r[0])+1),True)
            return ((max(l[0],r[0])+1),False)
        ans=height(root)
        return ans[1]