"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def newNode(node):
            return Node(node.val)
        ans=[]
        hash_edge={}
        visited={}
        def dfs(node,hash_edge,visited):
            if node is None:
                return 
            if node in visited:
                return
            visited[node]=True
            if node not in hash_edge:
                new_node=newNode(node)
                hash_edge[node]=new_node
            for i in node.neighbors:
                dfs(i,hash_edge,visited)
                hash_edge[node].neighbors.append(hash_edge[i])
            return
        if node==None:
            return None

        dfs(node,hash_edge,visited)
        return hash_edge[node]
                    
        