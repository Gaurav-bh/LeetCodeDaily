class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod=1000000007
        odd=0
        even=0
        curr_sum=0
        ans=0
        for i in arr:
            curr_sum+=i
            if curr_sum%2==1:
                ans=(ans+1)%mod
                ans=(ans+even)%mod
                odd=(odd+1)%mod
            else:
                ans=(ans+odd)%mod
                even=(even+1)%mod
        return ans%mod

        