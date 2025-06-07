class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        @lru_cache(None)
        def helper(row,col,):
            if row==1 or col==1 or (row+1)==col  :
                return 1
            return helper(row-1,col)+helper(row-1,col-1)

        grid=[1 for i in range(rowIndex+1)]
        for i in range(rowIndex+1):
            grid[i]=helper(rowIndex,i+1)
        return grid


        