textrules = open("day5input1.txt")
manuals = open("day5input2.txt")

#First compose the rules into a list of sorted pages
rules = []
for rule in textrules:
    rules.append([int(rule[0:2]), int(rule[3:5])])

ruledict = {}
for rule in rules:
    if rule[0] in ruledict:
        ruledict[rule[0]].append(rule[1])
    else:
        ruledict[rule[0]] = [rule[1]]

middleSum = 0
incorrectManuals = []
for manual in manuals:
    isSorted = True
    manual = [int(page) for page in manual.split(",")]
    for i in range(len(manual)-1):
        for j in range(i+1, len(manual)):
            if (manual[j] in ruledict) and (manual[i] in ruledict[manual[j]]):
                    isSorted = False
    if isSorted:
        middleSum += manual[int((len(manual)-1)/2)]
    else:
        incorrectManuals.append(manual)


print(middleSum)

#Do a DFS on the DAG to organize the pages
#ruledict = {10 : [11, 14, 17], 12 : [14, 17], 11 : [12]}

nodes = []
explored = {node : False for node in range(10, 100)}
def dfs(manual):
    nodes = []
    explored = {page : False for page in manual}
    def dfshelp(node):
        explored[node] = True
        if node in ruledict:
            for child in ruledict[node]:
                if child in manual and not explored[child]:
                    dfshelp(child)
        nodes.append(node)

    for node in manual:
        if not explored[node]:
            dfshelp(node)
    nodes.reverse()
    return nodes

middleSum = 0
for manual in incorrectManuals:
    sortManual = dfs(manual)
    middleSum += sortManual[int((len(sortManual) - 1)/2)]

print(middleSum)



textrules.close()
manuals.close()