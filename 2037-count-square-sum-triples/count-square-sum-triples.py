class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for i in range(1,n+1):
            for j in range(i,n+1):
                for k in range(j,n+1):
                    if i!=j and j!=k and (i*i+ j*j)==(k*k):
                        #print(i,j,k)
                        count +=2
        return count
        