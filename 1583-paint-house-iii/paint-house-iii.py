class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def recur(idx,neighborCount,prevColor):
            if idx==m:
                if neighborCount==target:
                    return 0
                else:
                    return math.inf+1
            mincost=math.inf
            if houses[idx]!=0:
                if houses[idx]==prevColor:
                    mincost= recur(idx+1,neighborCount,prevColor)
                else:
                    mincost= recur(idx+1,neighborCount+1,houses[idx])
            else:
                for i in range(n):
                    if i+1!=prevColor:
                        mincost=min(mincost,recur(idx+1,neighborCount+1,i+1)+cost[idx][i])
                    else:
                        mincost=min(mincost,recur(idx+1,neighborCount,i+1)+cost[idx][i])
            return mincost

        val= recur(0,0,0)
        if val==math.inf:
            return -1
        return val



        dp=[[math.inf for i in range(m)] for j in range(target)]
        

