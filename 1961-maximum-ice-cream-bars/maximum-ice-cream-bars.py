class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0 
        i = 0
        n = len(costs)
        while i<n and  coins >= costs[i]:
            coins -= costs[i]
            i+=1
        return i

        