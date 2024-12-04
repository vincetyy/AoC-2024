
moves = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]
chars = list("XMAS")

def check(x, y):
    global grid, moves, chars, length, breadth, ans
    
    for move in moves:
        char = 0
        newX = x
        newY = y
        for i in range(4):
            if (newX < 0 or newX >= breadth or newY < 0 or newY >= length):
                break
            currentChar = grid[newY][newX]
            if (currentChar != chars[char]):
                break
            if (i == 3):
                ans += 1
            else:
                newX += move[0]
                newY += move[1]
                char += 1

# Open the file in read mode
with open('input.txt', 'r') as file:
    # Loop through each line in the file
    ans = 0
    grid = []
    for line in file:
        grid.append(list(line.strip()))
    length = len(grid)
    breadth = len(grid[0])
    
    for x in range(breadth):
        for y in range(length):
            check(x, y)
    
    
    print (ans)