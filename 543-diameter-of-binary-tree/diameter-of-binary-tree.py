# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def diameter(root, ans):
            if root == None:
                return 0
            l = diameter(root.left, ans)
            r = diameter(root.right, ans)
            ans[0] = max(max(max(ans[0], l+r),l),r)
            return max(l,r)+1
        ans = [0]
        diameter(root, ans)
        return ans[0]
        