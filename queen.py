size=int(input())
board=list()
def createemptyboard(size): #Creates an empty board with 0's
    global board
    ar=list()
    for i in range (size):
        board.append(list())
        for j in range (size):
            board[i].append(0)
def rowindexof(n): #Returns row index (numbering starts from 0, 1, 2)
    global size
    return n//size
def columnindexof(n): #Returns column index
    global size
    return n%size
def updateboard(board,no): #Place a Queen denoted by no 2, and blocked places with 1
    global size
    b1=list(board)
    row=rowindexof(no)
    column=columnindexof(no)
    if b1[row][column]==0:
        b1[row][column]=2
        #Fill Vertically 1
        for i in range (size):
            if not(i==row):
                b1[i][column]=1

        #Fill Horizontally 1 
        for i in range (size):
            if not(i==column):
                b1[row][i]=1

        # Fill in \ direction
        num=no
        while num<(size**2)-(size+1):
            num+=size+1
            if b1[rowindexof(num)][columnindexof(num)]==0:
                b1[rowindexof(num)][columnindexof(num)]=1
                
        # Fill in / direction
        num=no
        while num>size-1:
            num-=size-1
            if b1[rowindexof(num)][columnindexof(num)]==0:
                b1[rowindexof(num)][columnindexof(num)]=1
        # Finally return
        return b1
    
def showboard(board): #Display the Board
    for i in range (len(board)):
        for j in range (len(board[0])):
            print (str(board[i][j]-1)+" ",end='')
        print ()
            
###########     MAIN-PROGRAM     ################
import copy
def goinside(board,column):
    global size
    save=copy.deepcopy(board)
    for i in range(size):
        board=copy.deepcopy(save)
        if board[i][column]==0:
            newb=updateboard(board,(i*size)+(column))
            if column==size-1:
                showboard(newb)
                return True #USED for breaking out of reccursive functions
            else:
                if (goinside(newb,column+1)):
                    return True
    if column==0:
        print("Not Possible")
    
createemptyboard(size)
goinside(board,0)

