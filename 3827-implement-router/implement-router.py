class DoubleLinkedNode:
    def __init__(self, value: tuple):
        self.value=value
        self.prev=None
        self.Next=None
    
    

class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit=memoryLimit
        self.packet_hash={}
        
        self.front=DoubleLinkedNode(())
        self.back=DoubleLinkedNode(())
        self.front.next=self.back
        self.back.prev=self.front
        self.back.next=self.front
        self.front.prev=self.back
        self.count=0
        self.dl = defaultdict(deque)
        

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source,destination,timestamp) in self.packet_hash:
            #print("present in hash")
            return False 
        if self.count==self.memoryLimit:
            self.forwardPacket()
        #print((source,destination,timestamp))
        curr_node=DoubleLinkedNode((source,destination,timestamp))
        
        self.packet_hash[(source,destination,timestamp)]=curr_node
        #add in linked list 
        self.count+=1
        self.dl[destination].append(timestamp)
        self.back.prev.next=curr_node
        curr_node.next=self.back
        curr_node.prev=self.back.prev
        self.back.prev=curr_node
        return True
        
        
        

    def forwardPacket(self) -> List[int]:
        if self.count==0:
            return []
        curr=self.front.next
        next=self.front.next.next
        next.prev=self.front
        self.front.next=next
        print(curr.value)
        del self.packet_hash[curr.value]
        self.dl[curr.value[1]].popleft()
        self.count-=1
        return list(curr.value)
        
            
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        tList = self.dl[destination]
        l, r = 0, len(tList) - 1
        while l <= r:
            m = l + (r - l) // 2
            if tList[m] >= startTime: r = m - 1
            else: l = m + 1
        leftMost = l

        l, r = 0, len(tList) - 1
        while l <= r:
            m = l + (r - l) // 2
            if tList[m] <= endTime: l = m + 1
            else: r = m - 1
        rightMost = r
        return rightMost - leftMost + 1
            
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)