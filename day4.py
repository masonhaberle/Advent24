inputs = open("day4input.txt")

ws = []

for line in inputs:
    ws.append([])
    for char in line:
        if char != "\n":
            ws[-1].append(char)

numHits = 0
for i in range(len(ws)):
    for j in range(len(ws) - 3):
        forward = ''.join(ws[i][j:j+4])
        down = ''.join([ws[j+k][i] for k in range(4)])
        numHits += (forward == "XMAS") + (forward == "SAMX") + (down == "XMAS") + (down == "SAMX")

for i in range(len(ws) - 3):
    for j in range(len(ws) - 3):
        diag = ''.join([ws[i+k][j+k] for k in range(4)])
        antidiag = ''.join([ws[len(ws)-1-(i+k)][j+k] for k in range(4)])
        numHits += (diag == "XMAS") + (diag == "SAMX") + (antidiag == "XMAS") + (antidiag == "SAMX")

print(numHits)

numHits = 0
for i in range(len(ws) - 2):
    for j in range(len(ws) - 2):
        diag = ''.join([ws[i+k][j+k] for k in range(3)])
        antidiag = ''.join([ws[i+2-k][j+k] for k in range(3)])
        numHits += ((diag == "MAS") or (diag == "SAM")) and ((antidiag == "MAS") or (antidiag == "SAM"))

print(numHits)