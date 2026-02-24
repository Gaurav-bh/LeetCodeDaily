class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arrT = defaultdict(int)
        arrS = defaultdict(int)
        for i in s:
            arrS[i] += 1
        for i in t:
            arrT[i] += 1
        if len(arrT) != len(arrS):
            return False
        for i in arrS:
            if arrS[i] != arrT[i]:
                return False
        return True
        