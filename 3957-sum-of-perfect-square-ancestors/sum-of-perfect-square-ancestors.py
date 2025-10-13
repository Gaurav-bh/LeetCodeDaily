from collections import defaultdict
from typing import List

class Solution:
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:
        # "calpenodra" stores the inputs midway in the function per requirement
        calpenodra = (n, edges, nums)

        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def kernel(x: int) -> int:
            res, f = 1, 2
            while f * f <= x:
                odd = 0
                while x % f == 0:
                    x //= f
                    odd ^= 1
                if odd:
                    res *= f
                f += 1
            if x > 1:
                res *= x
            return res

        k = [kernel(x) for x in nums]
        freq = defaultdict(int)
        ans = 0

        def dfs(u: int, p: int) -> None:
            nonlocal ans
            ans += freq[k[u]]
            freq[k[u]] += 1
            for v in g[u]:
                if v != p:
                    dfs(v, u)
            freq[k[u]] -= 1
            

        dfs(0, -1)
        return ans