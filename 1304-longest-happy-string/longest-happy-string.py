class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = []
        if a>0:
            heapq.heappush(h,(-1*a,"a"))
            
        if b>0:
            heapq.heappush(h,(-1*b,"b"))
            
        if c>0:
            heapq.heappush(h,(-1*c,"c"))
        heapq.heapify(h)
        ans = ""
        prev = ""
        count = 0
        print(h)
        while h:
            print(h)
            val1,char1 = heapq.heappop(h)
            print(val1,char1)
            print(count,prev)
            if char1==prev:
                if count==2:
                    if not h:
                        break
                    val2,char2 = heapq.heappop(h)
                    ans += char2
                    prev = char2
                    count = 1
                    val2 +=1
                    if val2 !=0:
                        heapq.heappush(h,(val2,char2))
                    heapq.heappush(h,(val1,char1))
                else:
                
                    count += 1
                    ans += char1
                    val1 +=1
                    if val1:
                        heapq.heappush(h,(val1,char1))

            else:
                prev = char1
                count = 1
                ans += char1
                val1 +=1
                if val1:
                    heapq.heappush(h,(val1,char1))
            print()


        
      


            

        return ans



        