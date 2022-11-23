def draw_triangle(height):
    for row_number in range(1, height + 1):
        num_blocks = row_number * 2 - 1
        num_spaces = height - row_number

        blocks = "^" * num_blocks
        spaces = " " * num_spaces

        row = f"{spaces}{blocks}"
        print(row)


draw_triangle(4)
draw_triangle(5)
