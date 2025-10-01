class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        rem = 0
        while numBottles:
            newBottle = (numBottles + rem)//numExchange
            rem = (numBottles + rem)%numExchange
            print(newBottle)
            numBottles = newBottle
            ans += numBottles
        return ans

            
        