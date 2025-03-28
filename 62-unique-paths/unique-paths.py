class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        if m==0 or n==0:
            return 0
        path=[[0 for i in range(n)] for j in range(m)]
        path[0][0]=1
        for i in range(m):
            for j in range(n):
                if i>0:
                    path[i][j]+=path[i-1][j]
                if j>0:
                    path[i][j]+=path[i][j-1]
        return path[m-1][n-1]