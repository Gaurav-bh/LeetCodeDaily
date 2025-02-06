class Solution:
    def findValidPair(self, s: str) -> str:
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in range(len(s)-1):
            if s[i]!=s[i+1] and dic[s[i]]==int(s[i]) and dic[s[i+1]]==int(s[i+1]):
                return s[i]+s[i+1]
        return ""
        