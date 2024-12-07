import re
inputs = open("day3input.txt")

fullmuls = []
for line in inputs:
    muls = re.findall("mul\\([0-9]+,[0-9]+\\)|do\\(\\)|don't\\(\\)", line)
    fullmuls += muls

total = 0
on = True
for mul in fullmuls:
    if mul == "do()":
        on = True
    elif mul == "don't()":
        on = False
    elif on:
        factors = re.findall("[0-9]+", mul)
        total += int(factors[0]) * int(factors[1])

print(total)