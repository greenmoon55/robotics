# -----------
# User Instructions:
#
# Modify the the search function so that it becomes
# an A* search algorithm as defined in the previous
# lectures.
#
# Your function should return the expanded grid
# which shows, for each element, the count when
# it was expanded or -1 if the element was never expanded.
#
# If there is no path from init to goal,
# the function should return the string 'fail'
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

heuristic = []
prev = [[None for col in range(len(grid[0]))] for row in range(len(grid))]

init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def generate_heuristic(grid, goal):

    heuristic = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            heuristic[x][y] = abs(goal[0] - x) + abs(goal[1] - y)

    return heuristic


def search(grid, init, goal, cost, heuristic):
    # ----------------------------------------
    # modify the code below
    # ----------------------------------------
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[init[0]][init[1]] = 1

    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    action = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]

    x = init[0]
    y = init[1]
    g = 0
    h = heuristic[x][y]
    f = g + h

    open = [[f, g, h, x, y]]

    found = False  # flag that is set when search is complete
    resign = False  # flag set if we can't find expand
    count = 0

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return "Fail"
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[3]
            y = next[4]
            g = next[1]
            expand[x][y] = count
            count += 1

            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            h2 = heuristic[x2][y2]
                            f2 = g2 + h2
                            open.append([f2, g2, h2, x2, y2])
                            closed[x2][y2] = 1
                            prev[x2][y2] = [x, y]
    return expand

if __name__ == "__main__":
    heuristic = generate_heuristic(grid, goal)
    res = search(grid, init, goal, cost, heuristic)
    for r in res:
        print r

    printed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    paths = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print i, j, res[i][j]
            if res[i][j] != -1:
                path = []
                x, y = i, j
                while prev[x][y]:
                    path.append([x, y])
                    nx = prev[x][y][0]
                    ny = prev[x][y][1]
                    x, y = nx, ny
                paths.append(path)
    for p in paths:
        print p

