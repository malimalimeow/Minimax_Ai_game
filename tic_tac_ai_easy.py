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
            

def ai_play(board,n):
        
    while True:
        row=random.randint(0,n-1)
        col=random.randint(0,n-1)
    
        if board[row][col]==" ":
            return row,col
        
       
def play(n):
    board=create_board(n)
    print_board(board)
    
    current_player="X"
    game=True
    
    
    while game:
        if current_player=="X":
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
        
        else:
            row,col=ai_play(board,n)
        
        board[row][col]=current_player
        if current_player=="X":
            current_player="O"
            
        else:
            current_player="X"
            
        
        print_board(board)
        game=check(board)
            
            
def check(board): 
    
    #row
    for row in board:
        if all(x=="X" for x in row):
            print("X wins")
            return False
    
        elif all(x=="O" for x in row):
            print("O wins")
            return False
    
    #col
    for col in range(len(board)):
        if all(board[row][col]=="X" for row in range(len(board))):
            print("X wins")
            return False
            
        elif all(board[row][col]=="O" for row in range(len(board))):
            print("O wins")
            return False
    
    #diagonal
    if all(board[col][col] == "X" for col in range(len(board))):
        print("X wins")
        return False
        
    elif all(board[col][col] == "O" for col in range(len(board))):
        print("O wins")
        return False
        
    if all(board[col][(len(board))-1-col] == "X" for col in range(len(board))):
        print("X wins")
        return False
        
    elif all(board[col][(len(board))-1-col] == "O" for col in range(len(board))):
        print("O wins")
        return False  
        
    elif all(x!=" " for row in board for x in row):
        print("draw.")
        return False
        
    return True
            
play(3)            
                