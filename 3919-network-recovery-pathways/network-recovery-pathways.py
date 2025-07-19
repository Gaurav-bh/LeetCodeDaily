class Solution:
    def findMaxPathScore(self, edges, online, k):
        graph, n = defaultdict(list), len(online)

        for u,v,c in edges:
            graph[u].append((v,c))

        def function(x):
            dict1 = {i:float("inf") for i in range(n)}

            dict1[0] = 0 

            stack = [(0,0)]

            while stack:
                cost,node = heapq.heappop(stack)

                for neighbor,c in graph[node]:
                    if dict1[neighbor] > cost+c and c >= x and online[neighbor] == True:
                        dict1[neighbor] = cost+c 
                        heapq.heappush(stack,(dict1[neighbor],neighbor))

            return dict1[n-1] <= k
        

        low, high = 0, 10**10

        while low <= high:
            mid = (low+high)//2 

            if function(mid):
                low = mid + 1 
            else:
                high = mid - 1 

        return high