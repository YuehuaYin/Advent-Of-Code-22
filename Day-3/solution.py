def getPriority(a):
    if ord(a) >= 97:
        return ord(a)-96
    else:
        return ord(a)-38

f = open("input.txt", "r")
lines = []
ans1 = 0
ans2 = 0
for line in f.readlines():
    lines.append(line[:len(line)-1])
    first = line[:len(line)//2]
    second = line[len(line)//2:]
    for i in first:
        if i in second:
            ans1 += getPriority(i)
            break
print(ans1)

g = 0
while g < len(lines):
    group = lines[g:g+3]
    for k in group[0]:
        if (k in group[1]) and (k in group[2]):
            ans2 += getPriority(k)
            break
    g += 3
print(ans2)
