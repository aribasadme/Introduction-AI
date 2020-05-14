"""
Tic Tac Toe Player
"""

import math
import copy
from collections import Counter

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
    # If game is over return
    if terminal(board):
        return

    # Count number of "X" and "O" pays
    c = Counter()
    for row in board:
        c.update(row)

    if (c[X] == c[O]):
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    acts = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                acts.add((i, j))
    return acts


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] == EMPTY:
        new_board = copy.deepcopy(board)
        new_board[i][j] = player(board)
        return new_board
    else:
        raise NameError('Action Invalid')


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontal win
    for i in range(3):
        if board[i][0] == [X, X, X]:
            return X
        elif board[i][0] == [O, O, O]:
            return O

    # Vertical win
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == X:
            return X
        elif board[0][i] == board[1][i] == board[2][i] == O:
            return O

    # Main diagonal win
    if board[0][0] == board[1][1] == board[2][2] == X:
        return X
    elif board[0][0] == board[1][1] == board[2][2] == O:
        return O

    # Opposite diagonal win
    if board[0][2] == board[1][1] == board[2][0] == X:
        return X
    elif board[0][2] == board[1][1] == board[2][0] == O:
        return O

    # There's a tie
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    if any([EMPTY in row for row in board]):
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal:
        return None
    if player(board) == X:
        best_val = -1
        best_move = (-1, -1)
        c = sum(row.count(EMPTY) for row in board)
        if c == 9:
            return best_move
        for action in actions(board):
            move_value = MIN_VALUE(result(board, action))
            if move_value == 1:
                best_move = action
                break
            if move_value > best_val:
                best_move = action
        return best_move
    if player(board) == O:
        best_val = -1
        best_move = (-1, -1)
        c = sum(row.count(EMPTY) for row in board)
        if c == 9:
            return best_move
        for action in actions(board):
            move_value = MAX_VALUE(result(board, action))
            if move_value == -1:
                best_move = action
                break
            if move_value < best_val:
                best_move = action
        return best_move


def MAX_VALUE(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, MIN_VALUE(result(board, action)))
        if v == 1:
            break
    return v


def MIN_VALUE(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = max(v, MAX_VALUE(result(board, action)))
        if v == -1:
            break
    return v
