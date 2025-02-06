class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dic={}
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                prod=nums[i]*nums[j]
                if prod in dic:
                    dic[prod]+=1
                else:
                    dic[prod]=1
        ans=0
        print(dic)
        for i in dic:
            if dic[i]>=2:
                #print(i,dic[i])
                #print("here:- ",))
                val=(((dic[i]*(dic[i]-1))//2)*8)
                #print("val:-",val)
                ans+=val
                print("ans:-",ans)
        return ans
        