class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[[heights[0],0]]
        maxarea=0
        n=len(heights)
        area=0
        for i in range(1,len(heights)):
            curr=heights[i]
            while len(stack) and stack[-1][0]>=curr:
                re=stack.pop()
                r=-1 if len(stack)==0 else stack[-1][1]
                area=(i-r-1)*re[0]
                maxarea=max(maxarea,area)
            stack.append([heights[i],i])
        #print(stack)
        while len(stack):
            curr=stack.pop()
            #print("yes")
            r=-1 if len(stack)==0 else stack[-1][1]
            area=curr[0]*(n-r-1)
            maxarea=max(maxarea,area)
       
            
            
        return maxarea
                
            
        