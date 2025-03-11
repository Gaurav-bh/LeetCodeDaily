class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        i=0
        n=len(s)
        while i<n:
            if s[i]=="]":
                curr=""
                while st[-1]!="[":
                    curr=st.pop()+curr
                st.pop()
                val=""
                while st and '0'<=st[-1]<='9':
                    val=st.pop()+val
                st.append(curr*int(val))
            else:
                st.append(s[i])
            i+=1
        ans=""
        for i in st:
            ans+=i
        return ans