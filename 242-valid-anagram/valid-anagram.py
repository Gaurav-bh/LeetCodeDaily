class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arrT = [0 for i in range(26)]
        arrS = [0 for i in range(26)]
        for i in s:
            arrS[ord(i)-ord('a')] += 1
        for i in t:
            arrT[ord(i)-ord('a')] += 1
        for i in range(26):
            if arrS[i] != arrT[i]:
                return False
        return True
        