class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=defaultdict(lambda:[])
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        # for i in adj:
        #     print(adj[i])
        
        def dfs(node,vertex,edge,visited,parent):
            visited[node]=True
            vertex[0]+=1

            for neighbor in adj[node]:
                
                if   visited[neighbor]==False:
                    edge[0]+=1
                    dfs(neighbor,vertex,edge,visited,node)
                if neighbor!=parent:
                    edge[0]+=1


        
        visited=[False for i in range(n)]
        count=0
        for i in range(n):
            edge=[0]
            vertex=[0]
            if  visited[i]==False:
                dfs(i,vertex,edge,visited,-1)
                print(visited)
                print("here",i,vertex,edge)
                if ((vertex[0]*(vertex[0]-1))//2)==edge[0]//2:
                    count+=1
                print("Count:- ",count)
        return count
        

        