class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        def calMaxAreahist(arr,n):
            print(arr)
            stack = []
            maxArea = 0
            for i in range(n):
                while stack and arr[stack[-1]]>=arr[i]:
                    val = stack.pop()
                    area = 0
                    if stack:
                        area = arr[val]*(i-stack[-1]-1)
                    else:
                        area = arr[val]*(i)
                    maxArea = max(area,maxArea)
                stack.append(i)
            #print(stack)
            while stack:
                val = stack.pop()
                area = 0
                if stack:
                    area = arr[val]*(n-stack[-1]-1)
                else:
                    area = arr[val]*(n)
                maxArea = max(area,maxArea)
            return maxArea
        k = [0 for i in range(m)]
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]=="1":
                    k[j]+=1
                else:
                    k[j] = 0
            ans = max(ans,calMaxAreahist(k,m))
        return ans
            
        
                    

        
        