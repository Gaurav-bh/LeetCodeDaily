class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        def check(n,s,memo):
            if n in memo:
                return memo[n]
            if n==0:
                return True
            if n==1 and 0 not in s:
                #print("yha pr")
                return True
            if n==3 and 1 not in s:
                #print("ussi pr")
                return True
           
            #print("n:-",n)
            i=0
            while 3**i<=n:
                if i not in s:
                    s.add(i)
                    if check(n-(3**i),s,memo):
                        memo[n]=True
                        return True
                    s.remove(i)
                #print("yes")
                i+=1
            memo[n]=False

            return False
        s=set(())
        memo={}
        return  check(n,s,memo)

        