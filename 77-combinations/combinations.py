class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        visited = [False for i in range(n)]
        def recur(curr,ind,ans,visited):
            print(ind)
            if len(curr)==k:
                ans.append(curr)
                return 
            for i in range(ind,n):
                if visited[i]==False:
                    visited[i]=True
                    recur(curr+[i+1],i,ans,visited)
                    visited[i]=False
        ans = []
        recur([], 0, ans, visited)
        return ans


        