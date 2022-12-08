import numpy as np


def moveInGrid(move: str, currentPos: list) -> list:
    direction = move[0]
    amount = int(move[1:])
    return [direction, amount]
    # print("dir: ", direction, " amount: ", amount)


Grid = np.ones((6, 6))

with open("3_input.txt") as puzzleIn:
    for wire in puzzleIn:
        currentPos = [2, 2]
        for moves in wire.split(","):
            direction = moves[0]
            amount = int(moves[1:])

            if direction == "R":
                res = np.insert(Grid[2][:], 0, 4)
                print(res)
                
                pass
            elif direction == "L":
                Grid[currentPos[0], currentPos[1]] = 2
                pass
            elif direction == "U":
                pass
            elif direction == "D":
                pass
            # moveInGrid(moves, currentPos)


print(Grid)
# print(Grid[0][0:])
