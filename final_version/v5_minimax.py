import random

def create_board(n):
    
    board=[]
    
    for i in range(0,n):
        row=[" "]* n
        board.append(row)
    
    return board

def print_board(board):
    separator="+".join(["---"]*(len(board)))
     
    for i in range(len(board)):
        print(" "+" | ".join(board[i]))
        if i < (len(board)-1):
            print(separator)

def minimax(board,depth,isMaximizing,alpha,beta):
            
    score=evaluate(board)
    
    if score!=None:
        if score==1:
            return 1000-depth
        
        elif score==-1:
            return -1000+depth
        
        else:
            return 0
    
    elif isMaximizing==True:
        best=-9999
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col]==" ":
                    board[row][col]="O"
                    value=minimax(board,depth+1,False,alpha,beta)
                    best=max(best,value)
                    alpha=max(best,alpha)
                    board[row][col]=" "
                    if beta<=alpha:
                        return best
        return best
                        
    elif isMaximizing==False:
        best=9999
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col]==" ":
                    board[row][col]="X"
                    value=minimax(board,depth+1,True,alpha,beta)
                    best=min(best,value)
                    beta=min(best,beta)
                    board[row][col]=" "
                    if beta<=alpha:
                        return best
        return best
                                                               
def ai_play_hard(board,n):
    
    best=-9999
    best_move=None
    
    for row in range(n):
        for col in range(n):
            if board[row][col]==" ":
                board[row][col]="O"
                score=minimax(board,0,False,-9999,9999)
                if score!= None:
                    if score > best:
                        best=score
                        best_move=row,col
                board[row][col]=" "
          
    return best_move
                     
def ai_play_mid(board,n):
    
    for row in range(n):
        for col in range(n):
            if board[row][col]==" ":
                board[row][col]="X"
                if evaluate(board)== -1 or evaluate(board)== 0:
                    board[row][col]=" "
                    return row,col
                board[row][col]=" "

    for row in range(n):
        for col in range(n):
            if board[row][col]==" ":
                board[row][col]="O"
                if evaluate(board)== +1 or evaluate(board)== 0:
                    board[row][col]=" "
                    return row,col
                board[row][col]=" "
                    
    while True:
        row=random.randint(0,n-1)
        col=random.randint(0,n-1)
    
        if board[row][col]==" ":
            return row,col
        
def ai_play_easy(board,n):  
    while True:
        row=random.randint(0,n-1)
        col=random.randint(0,n-1)
    
        if board[row][col]==" ":
            return row,col
          
def evaluate(board):
    #define k
    k=0
    n=len(board)
    if n<6:
        k=n
    
    else:
        k=5
    
    for row in range(n):
        for col in range(n):
            if col + (k-1) < n:
                if all(board[row][col+i]=="X" for i in range(k)):
                    return -1
                elif all(board[row][col+i]=="O" for i in range(k)):
                    return 1
                
            if row + (k-1) < n:
                if all(board[row+i][col]=="X" for i in range(k)):
                    return -1
                elif all(board[row+i][col]=="O" for i in range(k)):
                    return 1
                    
            if row+ (k-1)<n and col+(k-1)<n:
                if all(board[row+i][col+i]=="X" for i in range(k)):
                    return -1
                
                elif all(board[row+i][col+i]=="O" for i in range(k)):
                    return 1
                
            if row + (k-1) < n and col - (k -1) >= 0:
                if all(board[row+i][col-i]=="X" for i in range(k)):
                    return -1
                
                elif all(board[row+i][col-i]=="O" for i in range(k)):
                    return 1
                        
    if all(x!=" " for row in board for x in row):
        return 0
            
    return None
           
    
    
def play(n):
    if n > 6:
        print("Coming soon!:D\n The maximum board length is 6 for now.")
        return
        
    board=create_board(n)
    print_board(board)
    
    current_player="X"
    game=True
    
    while True:
        try:
            mode=int(input("Please choose the mode.(input number)\n 1. Easy level \n 2. Medium level\n 3. Hard level.\n"))
        except ValueError:
            print("Please input valid number.")
            continue
    
        if not mode in [1,2,3]:
            print("Please input valid number.")
            continue
        
        break
    
    empty=0
    while game:
        
        if current_player=="X":
            print("player'X'turn")
            try:
                row=int(input("row:"))
                col=int(input("col:"))
        
            except ValueError:
                print("please input valid row and col.")
                continue
        
            if row<0 or row>=n or col<0 or col>=n:
                print("please input valid row and col.")
                continue

            elif board[row][col]!=" ":
                print("please input valid row and col.")
                continue  
        
        elif mode == 1:
            row,col=ai_play_easy(board,n)
        
        elif mode ==2:
            row,col=ai_play_mid(board,n)
            
        elif mode ==3:
            for row in range(n):
                for col in range(n):
                    if board[row][col]==" ":
                        empty+=1
                
            if empty>9:
                row,col=ai_play_mid(board,n)
            else:
                row,col=ai_play_hard(board,n)
        
        board[row][col]=current_player
        if current_player=="X":
            current_player="O"
            print("player 'O' turn")
            
        else:
            current_player="X"
            
        
        print_board(board)
        game=check(board)
            
          
def check(board):    
    #define k
    k=0
    n=len(board)
    if n<6:
        k=n
    
    else:
        k=5
    
    for row in range(n):
        for col in range(n):
            if col + (k-1) < n:
                if all(board[row][col+i]=="X" for i in range(k)):
                    print("X wins")
                    return False
                elif all(board[row][col+i]=="O" for i in range(k)):
                    print("O wins")
                    return False
                
            if row + (k-1) < n:
                if all(board[row+i][col]=="X" for i in range(k)):
                    print("X wins")
                    return False
                elif all(board[row+i][col]=="O" for i in range(k)):
                    print("O wins")
                    return False

            if row+(k-1)<n and col+(k-1)<n:
                if all(board[row+i][col+i]=="X" for i in range(k)):
                    print("X wins")
                    return False
                
                elif all(board[row+i][col+i]=="O" for i in range(k)):
                    print("O wins")
                    return False
                
            if row + (k-1) < n and col -(k -1) >= 0:
                if all(board[row+i][col-i]=="X" for i in range(k)):
                    print("X wins")
                    return False
                elif all(board[row+i][col-i]=="O" for i in range(k)):
                    print("O wins")
                    return False
                        
    if all(x!=" " for row in board for x in row):
        print("draw")
        return False
    
    return True
        
                    

play(5)           


