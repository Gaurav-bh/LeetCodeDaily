class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        n = len(pizzas)
        k = n//4
        ans = 0
        print(pizzas)
        while k:
            c = (k+1)//2
            while c:
                ans += pizzas[n-1]
                c-=1
                k-=1
                n -= 1
        
            while k:
                ans += pizzas[n-2]
                k-=1
                n-=2
        return ans
        
        