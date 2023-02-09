#def display_gameboard():
#    for row in gameboard:
#        print(row)
#
#
#row1 = ["_", "_", "_"]
#row2 = ["_", "_", "_"]
#row3 = ["_", "_", "_"]
#
#gameboard = [row1, row2, row3]
#
#display_gameboard()


def display_gameboard():
    print(*gameboard, sep="\n")


gameboard = [["_"] * 3] * 3
display_gameboard()

