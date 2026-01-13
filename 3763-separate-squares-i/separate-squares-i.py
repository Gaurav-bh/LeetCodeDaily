class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        totalArea,yMax = 0, 0
        
        for x, y, l in squares:
            yMax = max(yMax, y+l)
            totalArea += l**2
        

        def check(yInc):
            area = 0
            for x,y,l in squares:
                if y< yInc:
                    area += l*min(yInc-y,l)
            return area >= totalArea/2
        

        lo = 0 
        hi = yMax
        eps = 1e-5
        #area()
        while abs(hi-lo)>eps:
            mid = (hi+lo)/2
            print(mid)
            if check(mid):
                hi = mid
            else:
                lo = mid
        return hi