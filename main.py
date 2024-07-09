from pacman import *
board = Board()
for i in board.pacman_map:
    for j in i:
        print(j+" ", end="")
    print()