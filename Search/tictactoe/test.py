from tictactoe import *

print(player(
    [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
))

print(player(
    [[X, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
))

print(actions(
    [[EMPTY, EMPTY, EMPTY],
            [X, EMPTY, O],
            [EMPTY, EMPTY, EMPTY]]
))

print(actions(
    [[EMPTY, EMPTY, EMPTY],
            [EMPTY, O, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
))

print(result(
    [[EMPTY, EMPTY, EMPTY],
            [EMPTY, O, EMPTY],
            [EMPTY, EMPTY, EMPTY]], (0, 1)
))

print(result(
    [[X, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]], (1, 2)
))
