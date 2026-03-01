class Solution:
    def minPartitions(self, n: str) -> int:
        ans = 0
        for i in n:
            charVal = ord(i)-48
            if charVal>ans:
                ans = charVal
        return ans

        