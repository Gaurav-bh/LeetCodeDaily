class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        distinct={}
        balls={}
        ans=[]
        for i in queries:
            if i[0] in balls:
                val=balls[i[0]]
                balls[i[0]]=i[1]
                if distinct[val]==1:
                    del distinct[val]
                else:
                    distinct[val]-=1
                if i[1] in distinct:
                    distinct[i[1]]+=1
                else:
                    distinct[i[1]]=1
            else:
                balls[i[0]]=i[1]
                if i[1] in distinct:
                    distinct[i[1]]+=1
                else:
                    distinct[i[1]]=1
            ans.append(len(distinct))
        return ans

        