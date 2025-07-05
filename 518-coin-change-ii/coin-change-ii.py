class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)

        noOfCombinations=[0]*(amount+1)
        noOfCombinations[0]=1
        for i in coins:
            for j in range(i,amount+1):
            
                noOfCombinations[j]+=noOfCombinations[j-i]
        print(noOfCombinations)
        return noOfCombinations[amount]

        