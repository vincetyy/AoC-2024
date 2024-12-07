
        
def getVisited(grid, x, y):
    visited = set()
    idx = 0
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
            
    return visited
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
    visited = getVisited(grid, startingX, startingY)
    # brute force setting of #
    for changedX, changedY in visited:
        currentSymbol = grid[changedY][changedX]
        if (currentSymbol == "#" or currentSymbol == "^"):
            continue
        grid[changedY][changedX] = "#"
        print (changedX, changedY)
        if (check(grid, startingX, startingY)):
            ans += 1
        grid[changedY][changedX] = currentSymbol
    
    print (ans)