import bisect
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        ans = []
        for i in spells:
            val = success//i
            if success%i!=0:
                val = val+1
            print("val;",val)
            ind = bisect.bisect_left(potions,val)
            print(ind)
            ans.append(n-ind)
        return ans
        

        