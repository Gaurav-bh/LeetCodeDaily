class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        d1 = d[0]
        d2 = d[1]
        r1 = r[0]
        r2 = r[1]
        lcm = ((r1*r2)//gcd(r1,r2))
        def canComplete(time):
            availableTime = time - (time//lcm)
            slots1 = time - (time // r1)
            
            # 2. Check Drone 2 capacity
            slots2 = time - (time // r2)
            if (slots1 >= d1) and (slots2 >= d2)  and availableTime>= d1+d2:
                return True
            return False


        low = d1+d2
        high = 2*low*2
        ans = high
        while low<=high:
            mid = (low+high)//2
            if canComplete(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return high +1
        
        

        