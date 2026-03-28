# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        def good(root, curr):
            if root == None:
                return 

            if curr<= root.val:
                count[0] += 1
            good(root.left, max(curr,root.val))
            
            good(root.right, max(curr,root.val))

        good(root, -100000)
        return count[0]