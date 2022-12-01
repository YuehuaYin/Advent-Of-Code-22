f = open("input.txt", "r")
counts = []
count = 0
for line in f.readlines():
    if line == "\n":
        counts.append(count)
        count = 0
    else:
        count += int(line)
print(max(counts))
counts.sort(reverse=True)
print(sum(counts[:3]))