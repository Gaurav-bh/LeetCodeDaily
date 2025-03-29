class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        for i in range(1,n):
            m=len(triangle[i])
            print(triangle[i])
            for j in range(m):
                if j==0:
                    triangle[i][j]=triangle[i-1][j]+triangle[i][j]
                elif j==(m-1):
                     triangle[i][j]=triangle[i-1][j-1]+triangle[i][j]
                else:
                    #print(""i,j)
                    print(m)
                    print(triangle[i][j])
                    print(triangle[i-1][j])
                    #print(traiangle[i-1][j-1])

                    triangle[i][j]=min(triangle[i-1][j],triangle[i-1][j-1])+triangle[i][j]
        return min(triangle[-1])

            
        