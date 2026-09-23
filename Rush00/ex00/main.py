#!/usr/bin/env python3

from checkmate import checkmate

def main():
    board1 = """\
R...
.K..
..P.
....\
"""
    board2 = """\
..
.K\
"""

    checkmate(board1)

if __name__ == "__main__":
    main()