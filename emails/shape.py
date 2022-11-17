def build_pyramid(height):
    num_bricks = height * 2

    for row in range(1, num_bricks, 2):
        spaces = " " * (num_bricks - row + 1)
        print(spaces, end="")
        for _ in range(row):
            print('^ ', end="")
        print()

    print()


build_pyramid(3)
build_pyramid(6)
build_pyramid(12)
