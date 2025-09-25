class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        phone={"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        n=len(digits)
        def help(ind,curr,res):
            if ind==n:
                res.append(curr)
                return
            for i in phone[digits[ind]]:
                help(ind+1,curr+i,res)
        res=[]
        curr=""
        ind=0
        help(ind,curr,res)
       
        return res
                