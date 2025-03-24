class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        i=0
        j=0
        noOfMeetings=len(meetings)
        count=0
        while j<noOfMeetings and i<=days:
            currMeet=meetings[j]
            print(currMeet,i,count)
            if currMeet[0]>i:
                count+=currMeet[0]-i-1
            i=max(i,currMeet[1])
            j+=1
        if i<days:
            count+=days-i
        return count