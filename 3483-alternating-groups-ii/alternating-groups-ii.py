class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        temp=colors+colors
        i=1
        w=1
        ans=0
        n=len(colors)
        while i<n+k-1:
            if temp[i]!=temp[i-1]:
                w+=1
            else:
                w=1
            i+=1
            if w>=k:
                ans+=1
        return ans




        