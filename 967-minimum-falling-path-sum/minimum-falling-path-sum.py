class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        paths=[[0 for i in range(n)] for j in range(m) ]
        paths[0]=matrix[0]
        if n==1:
            return matrix[0][0]

        for i in range(1,m):
            for j in range(n):
                if j==0:
                    paths[i][j]=matrix[i][j]+min(paths[i-1][j],paths[i-1][j+1])
                elif j==n-1:
                    paths[i][j]=matrix[i][j]+min(paths[i-1][j],paths[i-1][j-1])
                else:
                    paths[i][j]=matrix[i][j]+min(min(paths[i-1][j],paths[i-1][j-1]),paths[i-1][j+1])
        print(paths)
        return min(paths[-1])

