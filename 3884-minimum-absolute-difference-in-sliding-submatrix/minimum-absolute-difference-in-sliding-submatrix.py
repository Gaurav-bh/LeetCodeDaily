class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        res=[]
        for i in range(m-k+1):
            sub_res=[]
            for j in range(n-k+1):
                temp=[]
                for outer in range(k):
                    for inner in range(k):
                        temp.append(grid[i+outer][j+inner])
                temp=list(set(temp))
                temp.sort()
                if len(temp)>1:
                    min_abs=1000000000
                else:
                     min_abs=0
                for neigh in range(len(temp)-1):
                    min_abs=min(min_abs,temp[neigh+1]-temp[neigh])
                sub_res.append(min_abs)
            res.append(sub_res)
        return res
                        
        