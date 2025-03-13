class Solution:
    def simplifyPath(self, path: str) -> str:
        dir=[]
        size=len(path)
        curr=""
        for i in range(size):
            if path[i]=="/":
                dir.append(curr)
                curr=""
            else:
                curr+=path[i]
        if curr!="":
            dir.append(curr)
        stack=[]
        for i in dir:
            print(stack)
            if i=="..":
                if stack:
                    stack.pop()
            elif i=="" or i==".":
                continue
            else:
                stack.append(i)
        ans=""
        while stack:
            ans+="/"+stack.pop(0)
        if  ans=="":
            return "/"
        return ans

        

        