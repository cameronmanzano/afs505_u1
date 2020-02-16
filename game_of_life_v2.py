# Cameron Manzano
# Group Member = Brian Eisenbarth
# Reviewer = Gunnar Newell
# 65/100

# Grid with rows and columns defined
def main():
    from sys import argv
    nrows = 30
    ncols = 80
    coords = argv[2:]
    grid = [[0]*(ncols + 1) for i in range(nrows + 1)]
    init_grid(coords, grid)
    print_grid(grid, nrows, ncols)
    max_ticks = int(argv[1])
    loop_count = 0

    while loop_count < max_ticks:
        grid = make_move(grid, ncols, nrows)
        print_grid(grid, nrows, ncols)
        loop_count += 1

# Initial grid with rows and columns defined
def init_grid(coords, grid):
    for i in range(len(coords)):
        row, col = coords[i].split(':')
        row = int(row)
        col = int(col)
        grid[row - 1][col - 1] = 1

# Determination of where the player will make his next move
def make_move(grid, ncol, nrow):
    new_grid = [[0] * (ncol + 1) for i in range(nrow + 1)]
    for i in range(nrow):
        for j in range(ncol):
            upper_left = grid[i - 1][j - 1]
            upper_center = grid[i - 1][j]
            upper_right = grid[i - 1][j + 1]
            center_left = grid[i][j - 1]
            center_center = grid[i][j]
            center_right = grid[i][j + 1]
            lower_left = grid[i + 1][j - 1]
            lower_center = grid[i + 1][j]
            lower_right = grid[i + 1][j + 1]
            on_neighbors = upper_left + upper_center + upper_right + center_left + center_right + lower_left + lower_right + lower_right
            if grid[i][j] == 1 and on_neighbors < 2:
                new_grid[i][j] = 0
            elif grid[i][j] == 1 and on_neighbors > 2 or on_neighbors > 3:
                new_grid[i][j] = 0
            elif grid[i][j] == 1 and on_neighbors > 3:
                new_grid[i][j] = 0
            else:
                return new_grid

# - defining off and X defining on
def print_grid(grid, nrows, ncols):
    for i in range(nrows):
        for j in range(ncols):
            if grid [i][j] == 0:
                print("-", end = "")
            else:
                print("X", end = "")
        print()
    print()




main()
