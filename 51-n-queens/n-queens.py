class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def valid(row,col,board):
            for i in range(n):
                if board[i][col]=='Q':
                    return False
            r=row
            c=col
            while r>-1 and c>-1:
                if board[r][c]=='Q':
                    return False
                r-=1
                c-=1
            r=row
            c=col
            while r>-1 and c<n:
                if board[r][c]=='Q':
                    return False
                r-=1
                c+=1
            return True
        
        def solve(board,ind,ans):
            if ind==n:
                
                for k in board:
                    print("curr",k)
                temp=[]
                for i in board:
                    temp.append("".join(i))
                ans.append(temp.copy())
                #print("res",res)
                return 

                return True
            for i in range(n):
                if valid(ind,i,board):
                    board[ind][i]='Q'
                    solve(board,ind+1,ans)
                
                    board[ind][i]="."
            

        
        
        
        ans=[]
        board=[["." for i in range(n)] for j in range(n)]
        
        
        solve(board,0,ans)
        return ans
                
            

            

        