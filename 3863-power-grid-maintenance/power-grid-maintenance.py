class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        def dfs(curr,visited,compId):
            visited[curr]=compId
            for i in graph[curr]:
                if  visited[i]==0:
                    dfs(i,visited,compId)
            

        
        graph=[[] for j in range(c+1)]
        for i in connections:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        #print(graph)
        visited=[0 for i in range(c+1)]
        listCompId=[]
        for i in range(1,c+1):
            if visited[i]==0:
                listCompId.append(i)
                dfs(i,visited,i)
        compListMain = defaultdict(list)
        for i in range(1 ,c+1):
            compListMain[visited[i]].append(i)
        active=[True for i in range(c+1)]
        res=[]
        for query in queries:
            i=query[1]
            if query[0]==1:
                if active[i]:
                    res.append(i)
                    continue
                else:
                    compId=visited[i]
                    while compListMain[compId] and active[compListMain[compId][0]] == False:
                        compListMain[compId].pop(0 )
                    res.append(compListMain[compId][0] if compListMain[compId] else -1)
            else:
                active[i]=False
                    
        return res





            


