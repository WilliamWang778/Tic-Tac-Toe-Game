"""
Tic Tac Toe Player
"""

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
    numberO = numberX = 0
    for row in board:
        for col in row:
            if col == O:
                numberO += 1
            if col == X:
                numberX += 1
    if numberO > numberX:
        return X
    elif numberO == numberX:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    emptySpots = set()
    for row in range(3):
        for col in range(3):
            chess = board[row][col]
            if chess == EMPTY:
                emptySpots.add((row, col))
    return emptySpots


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row = action[0]
    col = action[1]
    if row < 0 or row > 2 or col < 0 or col > 2:
        raise Exception

    new_board = initial_state()
    next_player = player(board)

    for r in range(3):
        for c in range(3):
            new_board[r][c] = board[r][c]

    new_board[row][col] = next_player
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    index = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
    ]
    for row in index:
        if (board[row[0][0]][row[0][1]] == board[row[1][0]][row[1][1]] == board[row[2][0]][row[2][1]] == O) or \
                (board[row[0][0]][row[0][1]] == board[row[1][0]][row[1][1]] == board[row[2][0]][row[2][1]] == X):
            return board[row[0][0]][row[0][1]]

    # Check columns
    index = [
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
    ]
    for col in index:
        if (board[col[0][0]][col[0][1]] == board[col[1][0]][col[1][1]] == board[col[2][0]][col[2][1]] == O) or \
                (board[col[0][0]][col[0][1]] == board[col[1][0]][col[1][1]] == board[col[2][0]][col[2][1]] == X):
            return board[col[0][0]][col[0][1]]

    # Check diagonals
    index = [
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    for dia in index:
        if (board[dia[0][0]][dia[0][1]] == board[dia[1][0]][dia[1][1]] == board[dia[2][0]][dia[2][1]] == O) or \
                (board[dia[0][0]][dia[0][1]] == board[dia[1][0]][dia[1][1]] == board[dia[2][0]][dia[2][1]] == X):
            return board[dia[0][0]][dia[0][1]]

    return EMPTY


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != EMPTY:
        return True

    numChess = 0
    for row in board:
        for col in row:
            if col != EMPTY:
                numChess += 1
    if numChess == 9:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == O:
        return -1
    elif win == X:
        return 1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    ai = player(board)
    points = actions(board)
    if ai == X:
        score = -99
        best_point = (-1, -1)
        for point in points:
            res = minimize(result(board, point))
            if res > score:
                score = res
                best_point = point
        return best_point
    else:
        score = 99
        best_point = (-1, -1)
        for point in points:
            res = maximize(result(board, point))
            if res < score:
                score = res
                best_point = point
        return best_point


def maximize(board):
    if terminal(board):
        return utility(board)

    next_state = actions(board)
    score = -99
    for point in next_state:
        score = max(score, minimize(result(board, point)))
    return score


def minimize(board):
    if terminal(board):
        return utility(board)

    next_state = actions(board)
    score = 99
    for point in next_state:
        score = min(score, maximize(result(board, point)))
    return score
