class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        
        if n==1:
            return matrix[0][0]

        for i in range(1,m):
            for j in range(n):
                if j==0:
                    matrix[i][j]=matrix[i][j]+min(matrix[i-1][j],matrix[i-1][j+1])
                elif j==n-1:
                    matrix[i][j]=matrix[i][j]+min(matrix[i-1][j],matrix[i-1][j-1])
                else:
                    matrix[i][j]=matrix[i][j]+min(min(matrix[i-1][j],matrix[i-1][j-1]),matrix[i-1][j+1])
        
        return min(matrix[-1])

