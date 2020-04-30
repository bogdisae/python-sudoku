import copy
import eel
import time
# eel.init('web') frontend files in directory 'web'
# eel.start('main.html') start page in directory web called main.html

eel.init('Frontend')

board = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
    ]
eel.jswrap(board)

def matrixConverter(list):
    board = [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]
    listpos = 0
    for row in range(0, 9):
        for number in range(0, 9):
            board[row][number] = list[listpos]
            listpos = listpos + 1
    return board

def setup(board):
    '''board = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
    ]'''
    position = 1
    for row in board:
        for number in row:
            if number != 0:
                eel.setup(position, number)
            position = position + 1
setup(board)


def possibilitiesCheck(board, col, row):
    possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    rowCheck = board[row]
    
    colCheck = [row[col] for row in board]
    
    if row < 3: 
        if col < 3:
            boxCheck =  [row[0:3] for row in board[:3]]
        elif col < 6:
            boxCheck =  [row[3:6] for row in board[:3]]
        else:
            boxCheck =  [row[6:] for row in board[:3]]
    elif row < 6:
        if col < 3:
            boxCheck =  [row[0:3] for row in board[3:6]]
        elif col < 6:
            boxCheck =  [row[3:6] for row in board[3:6]]
        else:
            boxCheck =  [row[6:] for row in board[3:6]]
    else:
        if col < 3:
            boxCheck =  [row[0:3] for row in board[6:]]
        elif col < 6:
            boxCheck =  [row[3:6] for row in board[6:]]
        else:
            boxCheck =  [row[6:] for row in board[6:]]
    
    matrixBoxCheck = boxCheck
    boxCheck = []
    for list in matrixBoxCheck:
        for number in list:
            boxCheck.append(number)

    #Check the box, row and column and find a number which could go here
    impossibilities = rowCheck + colCheck + boxCheck + [0]
    possibilities = [number for number in possibilities if number not in impossibilities]
    return possibilities

def solve(board):
    #Used to for permanent values
    boardCheck = copy.deepcopy(board)
    #Used to ensure a possibility for a box isnt re-used
    possibilityCount = [[0 for number in range(0, 9)] for number in range(0, 9)]
    row, col = 0, 0
    backtracking = False
    timeOut = 0
    while True : #and timeOut < 20:
        timeOut = timeOut + 1

        #Deal with row to column movement
        if col > 8:
            col, row = 0, row+1
        if row > 8:
            break
        if col < 0:
            col, row = 8, row - 1
        #Test print
        #print(board[row][col])
        #print('Row:', row, '\nCol:', col)
        if boardCheck[row][col] == 0:
            if backtracking == True:
                board[row][col] = 0
            #Number changing code
            possibilities = possibilitiesCheck(board, col, row)
            #print(possibilities)
            if len(possibilities) > 0:
                backtracking = False
                try:
                    board[row][col] = possibilities[possibilityCount[row][col]]
                    possibilityCount[row][col] = possibilityCount[row][col] + 1
                except:
                    backtracking = True
                    possibilityCount[row][col] = 0
                    col = col - 2
            else:
                col = col - 2
                backtracking = True
        elif backtracking == True:
            col = col - 2
        col = col + 1
        #for line in board:
            #print(line)
        #print('Backtracking:', backtracking)
    return board

@eel.expose
def check(board):
    board = matrixConverter(board)
    '''board = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
    ]'''
    board = solve(board)
    list = []
    for row in board:
        for number in row:
            list.append(number)
    return list

@eel.expose
def solveWithDisplay(board):
    board = matrixConverter(board)
    '''board = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
    ]'''
    #Used to for permanent values
    boardCheck = copy.deepcopy(board)
    #Used to ensure a possibility for a box isnt re-used
    possibilityCount = [[0 for number in range(0, 9)] for number in range(0, 9)]
    row, col = 0, 0
    backtracking = False
    timeOut = 0
    while True : #and timeOut < 20:
        timeOut = timeOut + 1

        #Deal with row to column movement
        if col > 8:
            col, row = 0, row+1
        if row > 8:
            break
        if col < 0:
            col, row = 8, row - 1
        #Test print
        #print(board[row][col])
        #print('Row:', row, '\nCol:', col)
        if boardCheck[row][col] == 0:
            if backtracking == True:
                board[row][col] = 0
            #Number changing code
            possibilities = possibilitiesCheck(board, col, row)
            #print(possibilities)
            if len(possibilities) > 0:
                backtracking = False
                try:
                    board[row][col] = possibilities[possibilityCount[row][col]]
                    possibilityCount[row][col] = possibilityCount[row][col] + 1
                except:
                    backtracking = True
                    possibilityCount[row][col] = 0
                    col = col - 2
                else:
                    #Send number to js
                    position = ((row*9) + col)+1
                    number = board[row][col]
                    time.sleep(.1)
                    eel.setup(position, number)
                    #---------- end of send number to js
            else:
                col = col - 2
                backtracking = True
        elif backtracking == True:
            col = col - 2
        col = col + 1
        #for line in board:
            #print(line)
        #print('Backtracking:', backtracking)
    return board

eel.start('sudoku.html')
#Send number to js
#position = ((row*9) + col)+1
#number = possibilities[possibilityCount[row][col]]
#eel.setup(position, number)
#---------- end of send number to js