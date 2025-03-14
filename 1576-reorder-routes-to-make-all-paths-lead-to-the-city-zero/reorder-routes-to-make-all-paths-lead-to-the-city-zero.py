class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(node, parent, adj, count):
            if node not in adj:
                return
            for neighbor, sign in adj[node]:
                if neighbor != parent:
                    count[0] += sign
                    dfs(neighbor, node, adj, count)

        
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append((v, 1))
            adj[v].append((u, 0))
        
        count = [0]
        dfs(0, -1, adj, count)
        return count[0]
            