class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ""
        for word in words:
            s = 0
            for j in word:
                s += weights[ord(j)-97]
            s = s%26
            ans += chr(97+(25-s))
        return ans
                
        