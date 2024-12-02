# Open the file in read mode
def check(line):
    length = len(line)
    if line[1] == line[0]:
        return False
    multiplier = 1 if line[1] > line[0] else -1
    for i in range(length - 1):
        diff = line[i + 1] - line[i]
        if (diff * multiplier > 3 or diff * multiplier < 1):
            return False
    return True

with open('input.txt', 'r') as file:
    # Loop through each line in the file
    ans = 0
    for line in file:
        line = list(map(int, line.strip().split()))
        length = len(line)
        if check(line):
            ans += 1
    print (ans)