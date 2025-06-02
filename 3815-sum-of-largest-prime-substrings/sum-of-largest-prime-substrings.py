class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        def prime(num):
            if num==1:
                return False
            for i in range(2,int(num**(1/2))+1):
                if num%i==0:
                    return False
            return True
            
        prime_nos=[]
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                val=int(s[i:j])
                #print(val)
                if prime(val):
                    prime_nos.append(val)
        prime_nos=list(set(prime_nos))
        prime_nos.sort(reverse=True)
        #print(prime_nos)
        if len(prime_nos)>3:
            return prime_nos[0]+prime_nos[1]+prime_nos[2]
        else:
            return sum(prime_nos)
                
        