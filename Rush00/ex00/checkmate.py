"""
Problems: King (K) is at checkmate position ?
Chesses: King (K), Pawn (P), Bishop (B), Rook (R), Queen (Q)
Rules:
    1. หมากจะกินตัวแรกที่ขวางทางเดินของมันเท่านั้น
    2. กระดานจะเป็นรูปสี่เหลี่ยมจัตุรัส ขนาดเท่าไหร่ก็ได้
    3. มี King เพียงตัวเดียว และหมากตัวอื่นทั้งหมดคือศัตรู
    4. หาก King ถูกรุก ให้พิมพ์ว่า "Success" ตามด้วยบรรทัดใหม่ หากไม่ถูกรุก ให้พิมพ์ว่า "Fail" ตามด้วยบรรทัดใหม่
โปรแกรมต้องไม่ค้าง หรือวนลูปไม่สิ้นสุด หากเกิดข้อผิดพลาดที่ไม่ได้ระบุไว้ ให้พิมพ์ข้อความ Error หรือไม่พิมพ์อะไรเลยแล้วคืนการควบคุมให้ผู้ใช้

Pawn (P): กินในแนวทะแยงด้านหน้า
Bishop (B): เดินและกินในแนวทะแยงได้ทุกทิศทาง
Rook (R): เดินและกินในแนวตรง (แนวตั้งและแนวนอน)
Queen (Q): เดินและกินได้ทั้งแนวตรงและแนวทะแยง (เหมือน Bishop + Rook)
"""

def checkmate(board_str):
    # if empty board
    if not board_str:
        print("Error")
        return

    board = [list(r) for r in board_str.splitlines()]
    size = len(board)
    # Check if board is not square
    if any(len(row) != size for row in board):
        print("Error")
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
        print("Error")
        return

    king_x, king_y = king_pos
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
                        # If found the King, Then checkmate
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
