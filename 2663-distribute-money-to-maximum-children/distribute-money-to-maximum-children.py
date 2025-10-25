class Solution:
    def distMoney(self, money: int, children: int) -> int:
        count = 0
        while money> children:
            if children==1:
                break
            if money-8 >= children-1:
                children -=1
                money -=8
                count +=1
            else:
                break
        print(money,children)
        if money==4 and children ==1:
            return count-1
        elif money ==8 and children ==1:
            return count+1
        if money < children:
            return -1
        return count
        
        
        