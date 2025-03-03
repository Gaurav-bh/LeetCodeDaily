# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(root,p,q):
            if root==None:
                return None
            if root==q or root==p:
                return root
            l=lca(root.left,p,q)
            r=lca(root.right,p,q)
            if r!=None and l!=None:
                return root
            elif r==None:
                return l
            else:
                return r	
        return lca(root,p,q)
        