import re
def textToNumber(lines):
    numberMap = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
        }
    for word, numb3r in numberMap.items():
        lines = lines.replace(word, str(numb3r))
    return lines
def process(lines):
    sumNumbers = 0
    for line in lines:
        number = re.findall(r'\d', textToNumber(line))
        sumNumbers += int(str(int(number[0])) + str(int(number[-1])))
    return sumNumbers
with open('day1-input.txt', 'r') as inputs:
    total = process(inputs.readlines())
print(total)


