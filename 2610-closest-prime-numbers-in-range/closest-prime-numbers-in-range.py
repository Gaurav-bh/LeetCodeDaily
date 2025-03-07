class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime=[True for i in range(1000001)]
        prime[1]=False
        for i in range(2,1000001):
            if prime[i]==True:
                temp=i*i
                while temp<1000001:
                    prime[temp]=False
                    temp+=i
        #print(prime[:20])
        primeList=[]
        for i in range(left,right+1):
            if prime[i]:
                primeList.append(i)
        #print(primeList)
        
        noOfPrimes=len(primeList)
        if len(primeList)<=1:
            return [-1,-1]
        minGap=math.inf
        ans=[-1,-1]
        for i in range(1,noOfPrimes):
            if (primeList[i]-primeList[i-1])<minGap:
                ans=[primeList[i-1],primeList[i]]
                minGap=primeList[i]-primeList[i-1]
        return ans
        
        