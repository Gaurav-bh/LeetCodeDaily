# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        s = 0
        def totalSum(root):
            nonlocal s
            if root==None:
                return 
            s += root.val
            totalSum(root.left)
            totalSum(root.right)
        def sum(root,ans ):
            nonlocal s
            if root==None:
                return 0
            if root.left == None and root.right==None:
                return root.val
            l = sum(root.left,ans)
            r = sum(root.right,ans)
            
            print("----",root.val)
            print(l,r)
            
            val1 = (s-l)*l
            val2 = (s-r)*r
            print(val1,val2)
            ans[0] = max(ans[0],max(val1,val2))
            return root.val+l+r
        totalSum(root)
        ans = [-99999999]
        sum(root,ans)
        return ans[0]%1000000007

        