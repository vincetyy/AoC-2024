with open('input.txt', 'r') as file:
    grid = []
    for line in file:
        grid.append(list(line.strip()))
    length = len(grid)
    breadth = len(grid[0])
    hashmap  = dict()
    antinode = set()
    
    for y in range(length):
        for x in range(breadth):
            element = grid[y][x]
            if (element == "."):
                continue
            hashmap[element] = hashmap.get(element, list())
            hashmap[element].append((x, y))
            
    for element in hashmap:
        coordinates = hashmap[element]
        for pos1 in coordinates:
            for pos2 in coordinates:
                if (pos1 == pos2):
                    continue
                i = 1
                while (True):
                    newX  = pos1[0] + (pos1[0] - pos2[0]) * i
                    newY  = pos1[1] + (pos1[1] - pos2[1]) * i
                    if (newX < 0 or newX >= breadth or newY < 0 or newY >= length):
                        break
                    antinode.add((newX, newY))
                    i += 1
                    
                i = -1
                while (True):
                    newX  = pos1[0] + (pos1[0] - pos2[0]) * i
                    newY  = pos1[1] + (pos1[1] - pos2[1]) * i
                    if (newX < 0 or newX >= breadth or newY < 0 or newY >= length):
                        break
                    antinode.add((newX, newY))
                    i -= 1
        

    print (len(antinode))