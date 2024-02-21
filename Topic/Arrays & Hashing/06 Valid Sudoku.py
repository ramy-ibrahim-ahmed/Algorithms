from collections import defaultdict


def isValidSudoku(board):
    for i in range(9):
        row_seen = set()
        col_seen = set()
        square_seen = set()

        for j in range(9):
            # Check rows
            if board[i][j] != ".":
                if board[i][j] in row_seen:
                    return False
                row_seen.add(board[i][j])

            # Check columns
            if board[j][i] != ".":
                if board[j][i] in col_seen:
                    return False
                col_seen.add(board[j][i])

            # Check squares
            square_row = 3 * (i // 3)
            square_col = 3 * (i % 3)
            if board[square_row + j // 3][square_col + j % 3] != ".":
                if board[square_row + j // 3][square_col + j % 3] in square_seen:
                    return False
                square_seen.add(board[square_row + j // 3][square_col + j % 3])
    return True


def isValidSudoku(board):
    rows = defaultdict(set)
    col = defaultdict(set)
    square = defaultdict(set)
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue
            else:
                if (
                    board[i][j] in rows[i]
                    or board[i][j] in col[j]
                    or board[i][j] in square[(3 * (i // 3) + j // 3)]
                ):
                    return False
                rows[i].add(board[i][j])
                col[j].add(board[i][j])
                square[(3 * (i // 3) + j // 3)].add(board[i][j])
    return True


# board = [
#     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", "6", "."],
#     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", "6", ".", ".", ".", ".", "2", "8", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
# ]
# print(isValidSudoku(board))

# board = [
#     ["8", "3", ".", ".", "7", ".", ".", ".", "."],
#     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", "6", "."],
#     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", "6", ".", ".", ".", ".", "2", "8", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
# ]
# print(isValidSudoku(board))