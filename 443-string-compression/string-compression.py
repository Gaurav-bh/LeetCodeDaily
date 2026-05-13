class Solution:
    def compress(self, chars: List[str]) -> int:
        count=0
        ans=""
        curr_char=""
        for char in chars:
            
            if char!=curr_char:
                if count<=1:
                    ans+=curr_char
                else:
                    ans+=curr_char+str(count)
                count=1
                curr_char=char
            else:
                count+=1
        if count<=1:
            ans+=curr_char
        else:
            ans+=curr_char+str(count)
        
        chars[:] = list(ans)
        
        #print(chars)
        


        return len(ans) 