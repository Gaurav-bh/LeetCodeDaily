# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')
        def max_rooted_at(node):
            if not node:
                return 0
            l = max(0, max_rooted_at(node.left))
            r = max(0, max_rooted_at(node.right))
            self.ans = max(self.ans, l + r + node.val)
            return max(l, r) + node.val
        max_rooted_at(root)
        return self.ans
            
        