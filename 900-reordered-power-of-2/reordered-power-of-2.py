class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        
        hash={}
        def hashValue(n):
            hashList=[]
            while n:
                hashList.append(n%10)
                n//=10
            hashList.sort()
            #print(hashList)
            string=""
            for i in hashList:
                string+=str(i)
            #print(string)
            return string

        temp=1
        i=0
        while i<32:
            temp=1<<i
            hash[hashValue(temp)]=True
            i+=1
        for i in hash:
            print(i)

        key=hashValue(n)
        if key in hash:
            return True
        return False
        
        