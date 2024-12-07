import re

with open("./data.txt", "r") as file:
    data = file.read()

pattern = r"mul\(\d+,\d+\)"

matches = re.findall(pattern, data)

total = 0
for match in matches:
    nums = match.split("mul(")[1].replace(")", "").split(",")
    total += int(nums[0]) * int(nums[1])

print(total)
