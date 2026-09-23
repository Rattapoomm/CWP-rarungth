def checkmate(board_str):
    # if empty board
    if not board_str:
        print("Error, The board must not be empty.")
        return

    board = [list(r) for r in board_str.splitlines()] # 2d list
    size = len(board)
    # Check if board is not square
    if any(len(row) != size for row in board):
        print("Error, The board must be square.")
        return

    directions = {
        "P": [(-1, -1), (-1, 1)],
        "B": [(-1, -1), (-1, 1), (1, -1), (1, 1)],
        "R": [(-1, 0), (1, 0), (0, -1), (0, 1)],
        "Q": [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)],
    }
    
    king_pos = None
    king_count = 0
    # Find King position
    for i in range(size):
        for j in range(len(board[i])):
            if board[i][j] == "K":
                king_pos = (i, j)
                king_count += 1

    # No king or more than 1 king
    if king_count != 1:
        print("Error, The board must have exactly one King.")
        return

    king_x, king_y = king_pos # king(x, y)
    # Check checkmate to the King
    for i in range(size):
        for j in range(len(board[i])):
            piece = board[i][j]
            if piece in directions:
                # Check all directions for each piece
                for dx, dy in directions[piece]:
                    x, y = i + dx, j + dy
                    # If the piece can move in that direction
                    while 0 <= x < size and 0 <= y < len(board[x]):
                        # If found the King, Then it's checkmate
                        if (x, y) == (king_x, king_y):
                            print("Success")
                            return

                        # Not king, Other piece blocking the way
                        if board[x][y] != ".":
                            break

                        # If pawn, it can only move can one step
                        if piece == "P":
                            break

                        x += dx
                        y += dy
    print("Fail")
