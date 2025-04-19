# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def recur(root,sum):
            
            if root.left==None and root.right==None:
                if sum+root.val==targetSum:
                    return True
                return False
            l=False
            r=False
            if root.left:
                l=recur(root.left,sum+root.val) 
            if root.right:
                r=recur(root.right,sum+root.val)
            return l or r
        if root==None:
            return False
        return recur(root,0)

        