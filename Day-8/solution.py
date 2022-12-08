f = open("input.txt", "r")
lines = []

for line in f.readlines():
    lines.append(line.strip())

ans1 = (len(lines) + len(lines[0])) * 2 - 4
ans2 = 0

for i in range (1, len(lines)-1):
    for j in range (1, len(lines[i])-1):
        left = lines[i][:j]
        right = lines[i][j+1:]
        up = []
        down = []
        for k in range (len(lines)):
            if k < i:
                up.append(lines[k][j])
            if k > i:
                down.append(lines[k][j])
        if lines[i][j] > max(left) or lines[i][j] > max(right) or lines[i][j] > max(up) or lines[i][j] > max(down):
            ans1 += 1

        ls = 0
        for l in left[::-1]:
            ls += 1
            if l >= lines[i][j]:
                break
        rs = 0
        for r in right:
            rs += 1
            if r >= lines[i][j]:
                break
        us = 0
        for u in up[::-1]:
            us += 1
            if u >= lines[i][j]:
                break
        ds = 0
        for d in down:
            ds += 1
            if d >= lines[i][j]:
                break
        if (ls*rs*us*ds) > ans2:
            ans2 = ls*rs*us*ds

print(ans1)
print(ans2)
