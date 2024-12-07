inputs = open("day2input.txt")

numLines = 0
for line in inputs:
    levels = [int(level) for level in line.split()]
    isUp = (levels[0] < levels[1])
    isSafe = True
    for i in range(len(levels) - 1):
        if isUp ^ (levels[i] < levels[i + 1]):
            isSafe = False
        diff = abs(levels[i+1] - levels[i])
        if diff == 0 or diff > 3:
            isSafe = False
    numLines += isSafe
print(numLines)

inputs.close()


inputs = open("day2input.txt")

numLines = 0
for line in inputs:
    levels = [int(level) for level in line.split()]
    isUp = ((levels[0] < levels[1]) + (levels[1] < levels[2]) + (levels[2] < levels[3])) > 1
    dampcheck = -1
    for i in range(len(levels) - 1):
        if isUp ^ (levels[i] < levels[i + 1]):
            dampcheck = i
        diff = abs(levels[i+1] - levels[i])
        if diff == 0 or diff > 3:
            dampcheck = i
    if dampcheck == -1:
        numLines += 1
    else:
        damped1 = list(levels)
        damped2 = list(levels)
        damped1.pop(dampcheck)
        damped2.pop(dampcheck+1)
        isDamped = False
        for dampedlist in [damped1, damped2]:
            isSafe = True
            for i in range(len(dampedlist) - 1):
                if isUp ^ (dampedlist[i] < dampedlist[i + 1]):
                    isSafe = False
                diff = abs(dampedlist[i+1] - dampedlist[i])
                if diff == 0 or diff > 3:
                    isSafe = False
            if isSafe:
                isDamped = True
        numLines += isDamped
            
print(numLines)

inputs.close()