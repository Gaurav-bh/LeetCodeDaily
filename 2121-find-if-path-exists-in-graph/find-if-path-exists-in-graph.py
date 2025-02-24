class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj=[[] for j in range(n)]
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        
        def dfs(curr,adj,visited):
            if curr==destination:
                return True
            visited[curr]=True
            for i in adj[curr]:
                if i not in visited:
                    if dfs(i,adj,visited):
                        return True
            return False
        visited={}
        return dfs(source,adj,visited)
        