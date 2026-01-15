class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        k = len(hBars)
        x = 1 if k else 0
        mX = 1 if k else 0
        print(hBars)
        print(vBars)
        for i in range(1,k):
            if hBars[i-1]+1==hBars[i]:
                x += 1
            else:
                
                x = 1
            mX = max(mX,x)
        
        print(mX)
        l = len(vBars)
        y = 1 if l else 0
        mY = 1 if l else 0
        for i in range(1,l):
            if vBars[i-1]+1==vBars[i]:
                y += 1
            else:
                
                y = 1
            mY = max(mY,y)
        print(mY)


        return min(mX+1,mY+1)**2
        