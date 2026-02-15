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
    if len(board)<6:
        k=len(board)
    
    else:
        k=5
    #row
    for row in board:
        result=line(row,k)
        if result!=None:
            return result
        
    #col
    for col in range(len(board)):
        col_line=[board[row][col] for row in range(len(board))]
        result=line(col_line,k)
        if result!=None:
            return result
       
    #diagonal
    dia_line=[board[col][col] for col in range(len(board))]
    result=line(dia_line,k)
    if result!=None:
        return result
        
    re_dia_line=[board[col][(len(board))-1-col] for col in range(len(board))]
    result=line(re_dia_line,k)
    if result!=None:
        return result
    
    if all(x!=" " for row in board for x in row):
        return 0
            
    return None
           
    
    
def play(n):
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
    if len(board)<6:
        k=len(board)
    
    else:
        k=5
    #row
    for row in board:
        result=line(row,k)
        if result== 1:
            print("O wins.")
            return False
    
        elif result== -1:
            print("X wins.")
            return False
                
    #col
    for col in range(len(board)):
        col_line=[board[row][col] for row in range(len(board))]
        result=line(col_line,k)
        if result== 1:
            print("O wins.")
            return False
    
        elif result== -1:
            print("X wins.")
            return False
       
    #diagonal
    dia_line=[board[col][col] for col in range(len(board))]
    result=line(dia_line,k)
    if result== 1:
        print("O wins.")
        return False
    
    elif result== -1:
        print("X wins.")
        return False
        
    re_dia_line=[board[col][(len(board))-1-col] for col in range(len(board))]
    result=line(re_dia_line,k)
    if result== 1:
        print("O wins.")
        return False
    
    elif result== -1:
        print("X wins.")
        return False
    
    if len(board)>=6:
        a=len(board)-5
        for i in range(a):
            col_dia_line=[board[col][col+i] for col in range(len(board)-i)]
            result=line(col_dia_line,k)
            if result== 1:
                print("O wins.")
                return False
    
            elif result== -1:
                print("X wins.")
                return False
            
            row_dia_line=[board[col+i][col] for col in range(len(board)-i)]
            result=line(row_dia_line,k)
            if result== 1:
                print("O wins.")
                return False
    
            elif result== -1:
                print("X wins.")
                return False
            
            for row in range(len(board)):
                for col in range(len(board)):
                    if row+k<len(board) and col-k-1>=0:
                        col_re_dia_line=[board[row+i][col-i] for i in range(k)]
                        result=line(col_re_dia_line,k)
                    if result== 1:
                        print("O wins.")
                        return False
    
                    elif result== -1:
                        print("X wins.")
                        return False
            
          
        
    
    if all(x!=" " for row in board for x in row):
        print("draw")
        return False
    
    return True
        
                    
def line(line,k):  
    count_o=0
    count_x=0
    
    for c in line:
        if c=="O":
            count_o+=1
            count_x=0
        elif c=="X":
            count_x+=1
            count_o=0
        else:
            count_o=0
            count_x=0
        
        if count_o==k:
            return +1
        elif count_x==k:
            return -1
    
                
play(7)           
