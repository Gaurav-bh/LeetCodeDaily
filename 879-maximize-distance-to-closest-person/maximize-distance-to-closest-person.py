class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        noOfSeats=len(seats)
        seatIndex=[]
        for i in range(noOfSeats):
            if seats[i]==1:
                seatIndex.append(i)
        maxDis=seatIndex[0]
        for i in range(1,len(seatIndex)):
            maxDis=max(maxDis,(seatIndex[i]-seatIndex[i-1])//2)
        maxDis=max(maxDis,noOfSeats-seatIndex[len(seatIndex)-1]-1)
        return maxDis
        