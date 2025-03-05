class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        stack=[]
        start=TreeNode(preorder[0])
        n=len(preorder)
        stack.append(start)
        #print(stack)
        for i in range(1,n):
            node,child=stack[-1],TreeNode(preorder[i])
            while stack and stack[-1].val<child.val:
                node=stack.pop()
            if node.val<child.val:
                node.right=child
            else:
                node.left=child
            stack.append(child)
            #print(stack)
        return start
