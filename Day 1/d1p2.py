# Open the file in read mode
with open('input.txt', 'r') as file:
    # Loop through each line in the file
    arr1 = list()
    arr2 = list()
    for line in file:
        line = line.strip().split("   ")
        val1 = int(line[0])
        val2 = int(line[1])
        arr1.append(val1)
        arr2.append(val2)
    arr1.sort()
    arr2.sort()
    ans = 0
    for i in range(len(arr1)):
        ans += arr1[i] * arr2.count(arr1[i])
    print (ans)