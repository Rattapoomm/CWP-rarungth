def checkmate_from_str(board: str) -> str:
    try:
        if not isinstance(board, str):
            return "Error"

        lines = board.strip("\n").split("\n")
        if not lines:
            return "Error"

        size = len(lines)
        for row in lines:
            if len(row) != size:
                return "Error"

        king_pos = None
        king_count = 0
        valid_pieces = {"K", "P", "B", "R", "Q"}

        for r in range(size):
            for c in range(size):
                if lines[r][c] == "K":
                    king_pos = (r, c)
                    king_count += 1

        if king_count != 1 or king_pos is None:
            return "Error"

        kr, kc = king_pos

        for pr, pc in [(kr + 1, kc - 1), (kr + 1, kc + 1)]:
            if 0 <= pr < size and 0 <= pc < size:
                if lines[pr][pc] == "P":
                    return "Success"

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = kr + dr, kc + dc
            while 0 <= r < size and 0 <= c < size:
                char = lines[r][c]
                if char in valid_pieces:
                    if char in ("R", "Q"):
                        return "Success"
                    break
                r += dr
                c += dc

        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            r, c = kr + dr, kc + dc
            while 0 <= r < size and 0 <= c < size:
                char = lines[r][c]
                if char in valid_pieces:
                    if char in ("B", "Q"):
                        return "Success"
                    break
                r += dr
                c += dc

        return "Fail"

    except Exception:
        return "Error"
