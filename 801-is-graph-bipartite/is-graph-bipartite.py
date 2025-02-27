class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        def dfs(curr,color,colors):
            colors[curr]=color
            for i in graph[curr]:
                if colors[i]==-1:
                    if not dfs(i,1-color,colors):
                        return False
                elif colors[i]==color:
                    return False
            return True
        colors=[-1]*n
        for i in range(n):
            if colors[i]==-1:
                if not dfs(i,0,colors):
                    return False
        return True
        