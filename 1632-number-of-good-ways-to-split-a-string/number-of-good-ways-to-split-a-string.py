class Solution:
    def numSplits(self, s: str) -> int:
        n=len(s)
        prefix=[0 for i in range(n)]
        suffix=[0 for i in range(n)]
        charSet=set()
        for i in range(n):
            charSet.add(s[i])
            prefix[i]=len(charSet)
        charSet=set()
        for i in range(n-1,-1,-1):
            charSet.add(s[i])
            suffix[i]=len(charSet)
        countWays=0
        for i in range(n-1):
            if prefix[i]==suffix[i+1]:
                countWays+=1
        return countWays