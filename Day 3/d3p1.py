import re
# Open the file in read mode
with open('input.txt', 'r') as file:
    # Loop through each line in the file
    ans = 0
    for line in file:
        eqns = re.findall(r'mul\(\d+,\d+\)', line)
        for eqn in eqns:
            nums = re.findall('\\d+', eqn)
            ans += int(nums[0]) * int(nums[1])
    print (ans)