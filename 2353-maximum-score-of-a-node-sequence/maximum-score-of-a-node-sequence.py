class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append([v, scores[v]])
            graph[v].append([u, scores[u]])            
            
        for u in graph:
            graph[u] = sorted(graph[u], key = lambda x: -x[1])[:3]
            
            
        res = -1
        for u, v in edges:
            # for each edge, find lu<->u<->v<->rv
            for lu, lscore in graph[u]:
                for rv, rscore in graph[v]:
                    if lu != v and lu != rv and rv != u:
                        res = max(res, scores[u] + scores[v] + lscore + rscore)
        return res

    