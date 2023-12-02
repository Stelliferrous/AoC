import re
sumNumbers = 0
with open("calibration-day1.txt", "r") as inputs:
    for string in inputs:
        numbers = re.findall(r"\d", string)
        sumNumbers += int(str(int(numbers[0])) + str(int(numbers[-1])))
print(sumNumbers)