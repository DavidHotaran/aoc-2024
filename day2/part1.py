with open("data.txt", "r") as file:
    data: list[str] = file.readlines()

total_safe = 0


def is_increasing(nums):
    prev = nums[0]
    is_good = False
    for num in nums[1:]:
        if num > prev and abs(num - prev) >= 1 and abs(num - prev) <= 3:
            is_good = True
        else:
            return False
        prev = num
    return is_good


def is_decreasing(nums):
    prev = nums[0]
    is_good = False
    for num in nums[1:]:
        if num < prev and abs(num - prev) >= 1 and abs(num - prev) <= 3:
            is_good = True
        else:
            return False
        prev = num
    return is_good


for line in data:
    report = [int(item) for item in line.strip().split(" ")]
    if report[0] < report[1]:
        if is_increasing(report):
            total_safe += 1
    elif report[0] > report[1]:
        if is_decreasing(report):
            total_safe += 1


print(total_safe)
