conditions = []
 
def check(order):
    global conditions
    length = len(order)
    for i in range(1, length):
        for j in range (i):
            prev = order[j]
            current = order[i]
            if [current, prev] in conditions:
                return False
    return True

def fix(order):
    global conditions, ans
    filteredConditions = []
    for condition in conditions:
        if condition[0] in order and condition[1] in order:
            filteredConditions.append(condition[0])
    arr = {}
    for element in order:
        arr[filteredConditions.count(element)] = element
    ans += int(arr[len(order) // 2])

# Open the file in read mode
with open('input.txt', 'r') as file:
    # Loop through each line in the file
    ans = 0
    isConditions = True
    conditions = []
    for line in file:
        if (line == "\n"):
            isConditions = False
            continue
        if (isConditions):
            conditions.append(line.strip().split("|"))
        else:
            order = line.strip().split(",")
            if (not check(order)):
                fix(order)

    print (ans)