class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        paths=[[0 for i in range(n)] for j in range(m)]
        if obstacleGrid[0][0]==1:
            return 0
        paths[0][0]=1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    paths[i][j]=0
                else:
                    if i>0:
                        paths[i][j]+=paths[i-1][j]
                    if j>0:
                        paths[i][j]+=paths[i][j-1]
        return paths[m-1][n-1]
        