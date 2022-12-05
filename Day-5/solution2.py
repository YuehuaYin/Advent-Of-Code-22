s1 = ['R','N','P','G']
s2 = ['T','J','B','L','C','S','V','H']
s3 = ['T','D','B','M','N','L']
s4 = ['R','V','P','S','B']
s5 = ['G','C','Q','S','W','M','V','H']
s6 = ['W','Q','S','C','D','B','J']
s7 = ['F','Q','L']
s8 = ['W','M','H','T','D','L','F','V']
s9 = ['L','P','B','V','M','J','F']
numToArr = {1:s1, 2:s2, 3:s3, 4:s4, 5:s5, 6:s6, 7:s7, 8:s8, 9:s9}

f = open("input.txt", "r")
for line in f.readlines():
    l = line.split(" ")
    for i in numToArr[int(l[3])][len(numToArr[int(l[3])])-int(l[1]):]:
        numToArr[int(l[5])].append(i)
    del numToArr[int(l[3])][len(numToArr[int(l[3])])-int(l[1]):]

for v in numToArr.values():
    print(v[-1], end="")