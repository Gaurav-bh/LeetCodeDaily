class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        
        def dfs(curr,adj,path,ans):
            
            if curr==(n-1):
                #path.append(curr)
                ans.append(path.copy())
                return
             
            for i in adj[curr]:
                if i not in path:
                    path.append(i)
                    dfs(i,adj,path,ans)
                    path.pop()          
            return 
        path=[0]
        ans=[]
        dfs(0,graph,path,ans)
        return ans
        
        