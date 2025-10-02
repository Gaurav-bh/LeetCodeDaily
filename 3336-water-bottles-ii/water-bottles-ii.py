class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty = 0
        ans = 0
        while (numBottles+empty)>=numExchange:
            print(numBottles, empty, numExchange)
            ans += numBottles
            empty += numBottles
            numBottles = 0
            if empty >= numExchange:
                empty -= numExchange
                numBottles = 1
            numExchange +=1
        return ans+numBottles



        