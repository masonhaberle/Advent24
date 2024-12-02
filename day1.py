inputs = open("day1input.txt")
ids1 = []
ids2 = []
for line in inputs:
    idpair = [int(item) for item in line.split()]
    ids1.append(idpair[0])
    ids2.append(idpair[1])

ids1.sort()
ids2.sort()

#Part 1
ans = 0
for i in range(len(ids1)):
    ans += abs(ids1[i] - ids2[i])
print(ans)

#Part 2
def similarityctr():
    ans = 0
    ids2ctr = 0
    for item in ids1:
        while item > ids2[ids2ctr]:
            ids2ctr += 1
            if ids2ctr >= len(ids2):
                return ans
        while item == ids2[ids2ctr]:
            ans += item
            ids2ctr += 1
    return ans
print(similarityctr())


inputs.close()