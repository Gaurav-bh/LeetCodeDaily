class Solution:
    def findColoredRoot(self, edges: list[list[int]], colors: str) -> int:
        colorMap = {"R":0, "B": 1, "W": 2}
        n = len(colors)

        indegree = [0 for i in range(n)]
        outdegree = [0 for i in range(n)]


        for u, v in edges:
            uColor = colorMap[colors[u]]
            vColor = colorMap[colors[v]]
            if uColor == vColor:
                return -1
            if (uColor +1)%3 == vColor:
                indegree[v] +=1
                outdegree[u] +=1
            else:
                indegree[u] +=1
                outdegree[v] +=1


        root = -1
        for i in range(n):
            if outdegree[i] >2:
                return -1
            if indegree[i] ==0:
                if root != -1:
                    return -1
                root = i
        return root
