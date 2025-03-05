# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def pathExpansion(path):
            s=""
            for i in range(len(path)):
                if i==(len(path)-1):
                    s+=str(path[i])
                else:
                    s+=str(path[i])+"->"
            return s
        def dfs(root,path,ans):
            print(root.val)
            if root==None:
                return 
            path.append(root.val)
            if root.left==None and root.right==None:
                #print("yes")
                ans.append(pathExpansion(path))
            else:
                
                if root.left:
                    dfs(root.left,path,ans)
                if root.right:
                    dfs(root.right,path,ans)
            path.pop()
        if root==None:
            return []
        ans=[]
        path=[]
        #print("Start")
        dfs(root,path,ans)
        print(ans)
        return ans
        