import math

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def distance(x1, y1, x2, y2):
            d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            return d
        maxArea = 0
        n = len(points)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                     
                    a = distance(x1,y1,x2,y2)
                    b = distance(x1,y1,x3,y3)
                    c = distance(x2,y2,x3,y3)

                    if a + b > c and a + c > b and b + c > a:                 
                        s = (a+b+c)/2
                        Area = math.sqrt((s*(s - a)*(s - b)*(s - c)))
                        maxArea = max(Area, maxArea)
        return maxArea
        