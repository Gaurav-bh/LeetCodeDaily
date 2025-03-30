class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        s_len=len(s)
        last_index=[-1 for i in range(26)]
        for i in range(s_len):
            last_index[ord(s[i])-97]=i
        i=0
        rev=last_index[ord(s[i])-97]
        #print(last_index)
        ans=[]
        last=-1
        while i<s_len:
            rev=last_index[ord(s[i])-97]
            while i<s_len and i<rev:
                #print(i,rev)
                rev=max(rev,last_index[ord(s[i])-97])
                i+=1
            ans.append(rev-last)
            last=rev
            i+=1
        return ans


        