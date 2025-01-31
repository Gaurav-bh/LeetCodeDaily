class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        val=[0]
        @lru_cache(None)
        def recur(amt):
            if amt==0:
                return 0
            val=math.inf
            for i in coins:
                if amt-i>=0:
                    val=min(val,1+recur(amt-i))
            return val
        
        val=recur(amount)
        print(val)
        if val==math.inf:
            return -1
        return val