with open("./data.txt", "r") as file:
    data = file.readlines()

list1, list2 = [], []
for row in data:
    num1, num2 = row.split("   ")
    list1.append(num1)
    list2.append(num2)

list1.sort()
list2.sort()
total = 0

for num1, num2 in zip(list1, list2):
    total += abs(int(num1) - int(num2))

print(total)
