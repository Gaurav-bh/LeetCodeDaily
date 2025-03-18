# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(root,dp):
            if root==None:
                return 0
            if root in dp:
                return dp[root]
            include=root.val
            if root.left!=None:
                include+=dfs(root.left.right,dp)+dfs(root.left.left,dp)
            if root.right!=None:
                include+=dfs(root.right.right,dp)+dfs(root.right.left,dp)
            exclude=dfs(root.left,dp)+dfs(root.right,dp)
            dp[root]=max(include,exclude)
            return dp[root]
        dp={}
        return  dfs(root,dp)
            
        