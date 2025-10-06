class Solution:
    dp = []
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:

        n = len(mat)
        m = len(mat[0])


        def valid(r,c):
            if r<0 or r>=n or c<0 or c>=m:
                return False
            return True
        ans = [[0 for i in range(m)] for j in range(n)]
        dp = self.createSumMatrix(mat)
        for i in range(n):
            for j in range(m):
                sum = self.sumRegion(max(i-k,0),max(j-k,0),min(i+k,n-1),min(j+k,m-1))
                #print(i,j,sum)
                ans[i][j] = sum
        return ans

    def createSumMatrix(self, matrix):
        
        rows, cols = len(matrix), len(matrix[0])
        self.dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for r in range(rows):
            for c in range(cols):
                self.dp[r + 1][c + 1] = (
                    self.dp[r + 1][c] +
                    self.dp[r][c + 1] +
                    matrix[r][c] -
                    self.dp[r][c]
                )
        

    def sumRegion(self, row1, col1, row2, col2 ):
        if not self.dp:
            return 0
        return (
            self.dp[row2 + 1][col2 + 1]
            - self.dp[row1][col2 + 1]
            - self.dp[row2 + 1][col1]
            + self.dp[row1][col1]
        )

       
                
     


