class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj=[[] for j in range(n)]
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        
        def bfs(source,adj,visited):
            q=[]
            q.append(source)
            visited[source]=True
            while q:
                curr=q.pop(0)
                if curr==destination:
                    return True
                for i in adj[curr]:
                    if i not in visited:
                        visited[i]=True
                        q.append(i)
            return False
        visited={}
        return bfs(source,adj,visited)
        