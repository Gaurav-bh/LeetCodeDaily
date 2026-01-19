class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n = len(mat)
        m = len(mat[0])
        prefix = [ [0 for i in range(m+1)] for j in range(n+1)]

        for i in range(1,n+1):
            for j in range(1,m+1):
                prefix[i][j] += mat[i-1][j-1]
                prefix[i][j] += prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

        def calculate(i, j):
            k = min(i, j)
            #print(i,j)
            for l in range(k,0,-1):
                s = prefix[i][j] - prefix[i-l][j] - prefix[i][j-l] + prefix[i-l][j-l]
                #print(s)
                if s <= threshold:
                    return l
            return 0                 
        
        maxS = 0
        for i in range(n):
            for j in range(m):
                maxS = max(maxS,calculate(i+1,j+1))
        return maxS
        