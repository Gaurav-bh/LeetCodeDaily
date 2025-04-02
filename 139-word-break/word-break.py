class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0]=True
        print(dp)
        for i in range(1,len(s)+1):
            for word in wordDict:
                # Make sure to stay in bounds while checking criteria
                if i >= (len(word)-1 ) and   dp[i - len(word)]:
                    if s[i - len(word)  : i ] == word:
                        dp[i] = True
                        
        
        return dp[-1]