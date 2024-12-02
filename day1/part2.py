from collections import defaultdict

with open("./data.txt", "r") as file:
    data = file.readlines()


counter = defaultdict(int)
list1, list2 = [], []
for row in data:
    num1, num2 = row.split("   ")
    list1.append(int(num1))
    counter[int(num2)] = counter[int(num2)] + 1

total = 0
for num in list1:
    total += num * counter[num]

print(total)
