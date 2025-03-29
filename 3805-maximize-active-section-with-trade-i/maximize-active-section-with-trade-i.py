class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        one=0
        zero=0
        zero_block=[]
        one_block=[]
        one_max_count=0
        zero_max_count=0
        
        for i in s:
            if i=="1":
                one+=1
                if zero>0:
                    zero_block.append(zero)
                zero_max_count=max(zero_max_count,zero)
                zero=0
            elif i=="0":
                zero+=1
        if zero!=0:
            zero_block.append(zero)
            zero_max_count=max(zero_max_count,zero)

        if len(zero_block)<2:
            print("idhar kya ")
            return one
        if one==0:
            print("nhi yha")
            return 0
        print("abs to yhi h ")
        zero_max_count=0
        for i in range(len(zero_block)-1):
            zero_max_count=max(zero_max_count,zero_block[i]+zero_block[i+1])

        return one+zero_max_count
        
                    
                
        