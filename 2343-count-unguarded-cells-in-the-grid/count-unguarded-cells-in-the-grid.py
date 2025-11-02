class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        def check(row,col):
            if row<0 or row>=m or col<0 or col>=n:
                return False
            return True
        
        def move(row,col,dir1,dir2,gird):
             
            
            #grid[row][col]=1
            newRow = row+dir1
            newCol = col+dir2
            if check(newRow,newCol) and (grid[newRow][newCol]==0 or grid[newRow][newCol]==1):
                grid[newRow][newCol]=1
                move(newRow,newCol,dir1,dir2,grid)

        grid =[ [0 for i in range(n)] for i in range(m)]
        #print(grid)

        for row,col in walls:
            grid[row][col] = 3
        for row,col in guards:
            grid[row][col] = 2

        for row,col in guards:
            
            move(row,col,-1,0,grid)
            move(row,col,1,0,grid)
            move(row,col,0,1,grid)
            move(row,col,0,-1,grid)


        for i in grid:
            print(i)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    count += 1
        return count
    

        
        