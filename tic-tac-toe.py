# board_size = 3 * 3
# print(" --- " * board_size)
# print("|   " * (board_size + 1))


def horiz_line():
    print(" --- " * board_size)

def vert_line():
    print("|   " * (board_size + 1))

# if __name__ == "__main__":
board_size = int(input("What size of game board? "))

for index in range(board_size):
#     horiz_line()
#     vert_line()
    print(horiz_line(), vert_line())