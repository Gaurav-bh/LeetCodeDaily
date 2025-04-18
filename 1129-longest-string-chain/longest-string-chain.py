class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_set=set(words)
        def dfs(currWord,MEMO):
            if currWord in MEMO:
                return MEMO[currWord]
            newWord=currWord
            maxLength=1
            for i in range(len(currWord)):
                newWord=currWord[:i]+currWord[i+1:]
                if newWord in word_set:
                    maxLength=max(maxLength,1+dfs(newWord,MEMO))
            MEMO[currWord]=maxLength
            return maxLength
        
        ans=0
        MEMO={}
        for word in words:
           
            ans=max(ans,dfs(word,MEMO))
        return ans
        