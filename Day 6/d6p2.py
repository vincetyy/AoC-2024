directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# returns the new idx, x and y positions after times moves
# return (-1, -1, -1) if move is out of bounds
def move(grid, idx, x, y, times):
    for _ in range(times):
        newX = x + directions[idx][0]
        newY = y + directions[idx][1]
        if (newX < 0 or newX >= breadth or newY < 0 or newY >= length):
            return (-1, -1, -1)
        if (grid[newY][newX] == "#"):
            idx = (idx + 1) % 4
        else:
            x = newX
            y = newY
    return (idx, x, y)

# returns True if grid causes a loop
def check(grid, x, y):
    
    # tortoise and hare to check for loop
    hareX = x
    hareY = y
    hareIdx = 0
    
    tortoiseX = x
    tortoiseY = y
    tortoiseIdx = 0
    while (True):
        hareIdx, hareX, hareY = move(grid, hareIdx, hareX, hareY, 2)
        tortoiseIdx, tortoiseX, tortoiseY = move(grid, tortoiseIdx, tortoiseX, tortoiseY, 1)
        if (hareIdx == -1):
            return False
        if (tortoiseX == hareX and tortoiseY == hareY and tortoiseIdx == hareIdx):
            return True

# Open the file in read mode
with open('input.txt', 'r') as file:
    # Loop through each line in the file
    grid = []
    
    ans = 0
    length = 0
    breadth = 0
    for line in file:
        grid.append(list(line.strip()))
        length += 1
    breadth = len(grid[0])
    
    
    for i in range(length):
        if ("^" in grid[i]):
            startingY = i
            startingX = grid[i].index("^")
    
    # brute force setting of #
    for changedX in range(breadth):
        for changedY in range(length):
            currentSymbol = grid[changedY][changedX]
            if (currentSymbol == "#" or currentSymbol == "^"):
                continue
            grid[changedY][changedX] = "#"
            print (changedX, changedY)
            if (check(grid, startingX, startingY)):
                ans += 1
            grid[changedY][changedX] = currentSymbol
    
    print (ans)