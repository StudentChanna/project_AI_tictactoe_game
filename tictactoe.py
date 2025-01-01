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
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count <= o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not EMPTY:
        raise ValueError("Invalid action")
    new_board = [row[:] for row in board]
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows for a winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]
    # Check columns for a winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not EMPTY:
            return board[0][col]
    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(EMPTY not in row for row in board)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        value = -math.inf
        best_action = None
        for action in actions(board):
            min_value = minimax_value(result(board, action), False)
            if min_value > value:
                value = min_value
                best_action = action
        return best_action
    else:
        value = math.inf
        best_action = None
        for action in actions(board):
            max_value = minimax_value(result(board, action), True)
            if max_value < value:
                value = max_value
                best_action = action
        return best_action


def minimax_value(board, maximizing):
    """
    Helper function for minimax to determine the value of a board state.
    """
    if terminal(board):
        return utility(board)

    if maximizing:
        value = -math.inf
        for action in actions(board):
            value = max(value, minimax_value(result(board, action), False))
        return value
    else:
        value = math.inf
        for action in actions(board):
            value = min(value, minimax_value(result(board, action), True))
        return value
