"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCnt = 0
    oCnt = 0

    for row in board:
        for cell in row:
            if (cell == X):
                xCnt += 1
            elif (cell == O):
                oCnt += 1
    
    if (xCnt >= oCnt):
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for idx, row in enumerate(board):
        for idy, cell in enumerate(row):
            if (cell == EMPTY):
                action.add((idx,idy))
            
    raise action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    res = copy.deepcopy(board)
    if (res(action[0], action[1]) != EMPTY ):
        raise NameError("Action not allowed")
    else:
       res[action[0]][action[1]] = player(res)
       return res


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if (board[0][0] == board[0][1] == board[0][2]):
        return board[0][0]
    elif (board[0][0] == board[1][0] == board[2][0]):
        return board[0][0]
    elif (board[0][0] == board[1][1] == board[2][2]):
        return board[0][0]
    elif (board[0][1] == board[1][1] == board[2][1]):
        return board[0][1]
    elif (board[0][2] == board[1][2] == board[2][2]):
        return board[0][2]
    elif (board[1][0] == board[1][1] == board[1][2]):
        return board[1][0]
    elif (board[2][0] == board[2][1] == board[2][2]):
        return board[2][0]
    elif (board[2][0] == board[1][1] == board[0][2]):
        return board[2][0]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check ig actions returns empty == no more moves 
    if (len(actions(board)) == 0 or winner(board) != None):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (winner(board) == X):
        return 1
    elif (winner(board) == O):
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
