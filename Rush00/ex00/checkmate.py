def checkmate(board: str) -> None:
    try:
        if not isinstance(board, str):
            return
        lines = board.strip("\n").split("\n")
        if not lines:
            return

        size = len(lines)

        #เช็คแถว NxN ไหม
        for row in lines:
            if len(row) != size:
                return 

        king_pos = None
        king_count = 0
        valid_pieces = {"K", "P", "B", "R", "Q"}

        #หา K 
        for r in range(size):
            for c in range(size):
                if lines[r][c] == "K":
                    king_pos = (r, c)
                    king_count += 1

        #เช็คว่ามี K แค่ตัวเดียวไหม
        if king_count != 1 or king_pos is None:
            return

        kr, kc = king_pos

        #คำนวณพิกัด 2 จุดที่ Pawn สามารถรุก King ได้
        pawn_attackers = [(kr + 1, kc - 1), (kr + 1, kc + 1)]
        
        #วนลูปดึงพิกัดที่ Pawn สามารถรุกได้มาเช็คทีละจุด 
        #ตรวจ Pawn
        for pr, pc in pawn_attackers:
            if 0 <= pr < size and 0 <= pc < size:
                if lines[pr][pc] == "P":
                    print("Success")
                    return

        #ตรวจ Rook และ Queen แนวตรง
        straight_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in straight_dirs:
            r, c = kr + dr, kc + dc
            while 0 <= r < size and 0 <= c < size:
                char = lines[r][c]
                if char in valid_pieces:
                    if char in ("R", "Q"):
                        print("Success")
                        return
                    else:

                        break
                r += dr
                c += dc

        #ตรวจ Bishop และ Queen แนวทแยง
        diag_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in diag_dirs:
            r, c = kr + dr, kc + dc
            while 0 <= r < size and 0 <= c < size:
                char = lines[r][c]
                if char in valid_pieces:
                    if char in ("B", "Q"):
                        print("Success")
                        return
                    else:

                        break
                r += dr
                c += dc

        print("Fail")

    except Exception:

        return print("Error")
