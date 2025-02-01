class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        paths=[[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                    #print(paths)
                    if i==0 and j==0:
                        paths[i][j]=grid[i][j]
                    elif i==0:
                        print(i,j)
                        paths[i][j]=grid[i][j]+paths[i][j-1]
                    elif j==0:
                        paths[i][j]=grid[i][j]+paths[i-1][j]
                    else:
                        paths[i][j]=grid[i][j]+min(paths[i-1][j],paths[i][j-1])
        #print(paths)
        return paths[m-1][n-1]

        