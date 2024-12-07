# Open the file in read mode
def check(values, idx, current, total):
    if (idx == len(values)):
        return current == total
    newVals = [current + values[idx], current * values[idx]]
    valid = False
    for val in newVals:
        valid |= check(values, idx + 1, val, total)
    return valid
    
with open('input.txt', 'r') as file:
    ans = 0
    for line in file:
        line = line.split(":")
        total = int(line[0])
        values = [int(x) for x in line[1].strip().split()]
        if (check(values, 0, 0, total)):
            ans += total
            
    print (ans)  