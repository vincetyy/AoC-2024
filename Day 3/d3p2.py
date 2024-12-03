import re
# Open the file in read mode
with open('input.txt', 'r') as file:
    # Loop through each line in the file
    ans = 0
    isDo = True
    for line in file:
        # i hate regex
        eqns = re.findall(r'(mul\(\d+,\d+\))|(do\(\))|(don\'t\(\))', line)
        # print (eqns)
        for eqn in eqns:
            if (eqn[0] != "" and isDo):
                nums = re.findall('\\d+', eqn[0])
                ans += int(nums[0]) * int(nums[1])
            elif (eqn[1] != ""):
                isDo = True
            else: 
                isDo = False
    print (ans)