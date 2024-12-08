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
                newX  = pos1[0] + pos1[0] - pos2[0]
                newY  = pos1[1] + pos1[1] - pos2[1]
                if (newX < 0 or newX >= breadth or newY < 0 or newY >= length):
                    continue
                antinode.add((newX, newY))
        
    print (len(antinode))