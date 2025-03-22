class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD=1000000007
        ans=1
        countSofa=0
        dic={}
        count=0
        size=len(corridor)
        for i in range(size):
            if corridor[i]=="S":
                count+=1
            if count>0 :
                if count not in dic:
                    dic[count]=i
        if count==0:
            return 0
        if count%2==1:
            return 0
        for i in range(2,count,2):
            countPot=0
            print(i)
            for j in range(dic[i],dic[i+1]):
                if corridor[j]=="P":
                    countPot+=1
            ans*=(countPot+1)%MOD
        return ans%MOD

#SPS PP SS P SSSS