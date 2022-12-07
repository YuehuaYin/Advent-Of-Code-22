f = open("input.txt", "r")
lines = []
sizes = {}
path = []
ans1 = 0

for line in f.readlines():
    lines.append(line.strip().split(" "))

for l in lines:
    if l[1] == "cd":
        if l[2] == "..":
            del path[-1]
        else:
            path.append(l[2])
            sizes["/".join(path)] = 0
    elif l[0] != "$" and l[0] != "dir":
        for i in range(len(path)):
            sizes["/".join(path[:i+1])] += int(l[0])

for s in sizes.values():
    if s < 100000:
        ans1 += s

needed = 30000000 - 70000000 + sizes["/"]
for t in sorted(sizes.values()):
    if t >= needed:
        ans2 = t
        break

print(ans1)
print(ans2)