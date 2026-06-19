class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ma = 0
        s = 0
        for al in gain:
            s += al
            ma = max(ma, s)
        return ma
        