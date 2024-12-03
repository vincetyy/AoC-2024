import re
# Open the file in read mode
with open('input.txt', 'r') as file:
    # Loop through each line in the file
    ans = 0
    for line in file:
        eqns = re.findall('mul\\([0-9]+,[0-9]+\\)', line)
        for eqn in eqns:
            nums = re.findall('[0-9]+', eqn)
            ans += int(nums[0]) * int(nums[1])
    print (ans)