class Solution:
    def countOdds(self, low: int, high: int) -> int:
        l = (high-low)+1
        if l&1:
            if low&1:
                return (l-1)//2+1
            return l//2
        else:
            return l//2
            
        