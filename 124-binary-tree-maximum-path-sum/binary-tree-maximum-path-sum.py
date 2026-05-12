# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxAns = [-10000]
        def calculate(root):
            if root == None:
                return 0

            l = max(0,calculate(root.left))
            r = max(0,calculate(root.right))
            maxAns[0] = max(maxAns[0], root.val+r+l)

            return max(l,r)+root.val
        calculate(root)
        return maxAns[0]

            
        