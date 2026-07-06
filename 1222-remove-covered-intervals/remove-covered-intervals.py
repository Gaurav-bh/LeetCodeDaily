class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        n=len(intervals)
        #print(intervals)
        max_=intervals[0][1]
        min_=intervals[0][0]
        count=1
        for i in range(1,n):
            #print(intervals[i])
            if intervals[i][1]<=max_:
                continue
            count+=1
            max_=max(max_,intervals[i][1])
            #print(count)
        return count
        