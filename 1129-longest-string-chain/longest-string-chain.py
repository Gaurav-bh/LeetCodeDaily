class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def dfs(currWord,MEMO):
            if currWord in MEMO:
                return MEMO[currWord]
            newWord=currWord
            maxLength=1
            for i in range(len(currWord)):
                newWord=currWord[:i]+currWord[i+1:]
                if newWord in words:
                    maxLength=max(maxLength,1+dfs(newWord,MEMO))
            MEMO[currWord]=maxLength
            return maxLength
        
        ans=0
        for word in words:
            MEMO={}
            ans=max(ans,dfs(word,MEMO))
        return ans
        