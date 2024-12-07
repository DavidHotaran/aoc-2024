import re

with open("./data.txt", "r") as file:
    data = file.read()

content = data.split("do()")
pattern = r"mul\(\d+,\d+\)"
total = 0

for line in content:
    match = line.split("don't()")
    good = match[0]
    # match[0] = good, match[1] = bad
    mul_match = re.findall(pattern, good)
    for item in mul_match:
        nums = item.split("mul(")[1].replace(")", "").split(",")
        total += int(nums[0]) * int(nums[1])

print(total)
