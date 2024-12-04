
moves = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
combinations = [list("MMSS")[i:] + list("MMSS")[:i] for i in range(4)]


def check(x, y):
    global grid, moves, chars, length, breadth, ans
    for combi in combinations:
        for i in range(4):

            newX = x + moves[i][0]
            newY = y + moves[i][1]
            if (newX < 0 or newX >= breadth or newY < 0 or newY >= length):
                break
            currentChar = grid[newY][newX]
            if (currentChar != combi[i]):
                break
            if (i == 3):
                ans += 1
                

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
            if (grid[y][x] == "A"):
                check(x, y)
    
    
    print (ans)