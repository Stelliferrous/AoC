import re
sumNumbers = 0
with open("day1-input.txt", "r") as inputs:
    for string in inputs:
        numbers = re.findall(r"\d", string)
        sumNumbers += int(str(int(numbers[0])) + str(int(numbers[-1])))
print(sumNumbers)