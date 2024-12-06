# Open the file in read mode
with open('input.txt', 'r') as file:
    # Loop through each line in the file
    grid = []
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    idx = 0
    ans = 1
    
    visited = set()
    
    length = 0
    breadth = 0
    for line in file:
        grid.append(list(line.strip()))
        length += 1
    breadth = len(grid[0])
    
    x = 0
    y = 0
    
    for i in range(length):
        if ("^" in grid[i]):
            y = i
            x = grid[i].index("^")
            visited.add((x, y))         
    
    while (True):
        newX = x + directions[idx][0]
        newY = y + directions[idx][1]
        if (newX < 0 or newX >= breadth or newY < 0 or newY >= length):
            break
        if (grid[newY][newX] == "#"):
            idx = (idx + 1) % 4
        else:
            visited.add((newX, newY))
            x = newX
            y = newY

    print (len(visited))