class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict=set(wordDict)
        n=len(s)
        dp={}
        def recursion(st,curr,ans):
            if len(st)==0:
                s=""
                l=len(curr)
                for i in range(l):
                    if i==l-1:
                        s+=curr[i]
                    else:
                        s+=curr[i]+" "
                ans.append(s)
                return True
            
            #print("ind",ind)
            for i in range(len(st)):
                #print('i:-',i)
                #print(st[:i+1])
                if st[:i+1] in wordDict:
                    #print("s",st)
                    #print(st[:i+1])
                    #print(st[i+1:])
                    curr.append(st[:i+1])
                    recursion(st[i+1:],curr,ans)
                    curr.pop()
           
            return False
        curr=[]
        ans=[]

        recursion(s,curr,ans)
        print(ans)
        return ans
        