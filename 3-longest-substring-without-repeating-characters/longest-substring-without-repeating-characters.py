class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_hash={}
        l=0
        r=0
        string_len=len(s)
        max_len=0
        while r<string_len:
            curr_char=s[r]
            while l<=r and curr_char in char_hash:
                del char_hash[s[l]]
                l+=1
            
            max_len=max(max_len,r-l+1)
            char_hash[curr_char]=True
            r+=1
        return max_len
        
            


        
        