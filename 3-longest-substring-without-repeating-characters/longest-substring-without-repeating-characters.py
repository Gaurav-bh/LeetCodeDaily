class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_hash={}
        l=0
        r=0
        string_len=len(s)
        max_len=0
        while r<string_len:
            curr_char=s[r]
            if curr_char in char_hash and l<char_hash[curr_char]+1:
                l=char_hash[curr_char]+1
            #print(l,r)
            max_len=max(max_len,r-l+1)
            char_hash[curr_char]=r
            r+=1
            #print(char_hash)
        return max_len
        
            


        
        