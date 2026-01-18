from sortedcontainers import SortedList
class AuctionSystem:

    def __init__(self):
        self.items = defaultdict(SortedList)
        self.users = defaultdict(int)
        

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        if (userId,itemId) in self.users:
            self.updateBid(userId,itemId,bidAmount)
        else:

            self.items[itemId].add((bidAmount,userId))
            self.users[(userId,itemId)] = bidAmount
        

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.items[itemId].remove((self.users[(userId,itemId)],userId))
        self.users[(userId,itemId)] = newAmount
        self.items[itemId].add((self.users[(userId,itemId)],userId))
          
        

    def removeBid(self, userId: int, itemId: int) -> None:
        # print(self.items)
        # print(userId,itemId)
        # print((self.users[userId]))
        self.items[itemId].remove((self.users[(userId,itemId)],userId))
        del self.users[(userId,itemId)]
        if len(self.items[itemId])==0:
            del self.items[itemId]
        
        

    def getHighestBidder(self, itemId: int) -> int:
        #print(self.items)
        if itemId in self.items:
            return self.items[itemId][-1][1]
        return -1
        


# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)