class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        def bfs(node,colors):
            colors[node]=0
            q = deque()
            q.append([node,0])
            while q:
                curr,color=q.popleft()
                for i in graph[curr]:
                    if colors[i]==-1:
                        colors[i]=1-color
                        q.append([i,1-color])
                    elif colors[i]==color:
                        return False
            return True

        colors=[-1]*n
        for i in range(n):
            if colors[i]==-1:
                if not bfs(i,colors):
                    return False
        return True
        