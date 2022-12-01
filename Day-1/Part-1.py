f = open("input.txt", "r")
counts = []
count = 0
deer = 0
for line in f.readlines():
    if line == "\n":
        deer += 1
        counts.append(count)
        count = 0
    else:
        count += int(line)
print(max(counts))