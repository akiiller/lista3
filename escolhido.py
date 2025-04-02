

rows = int(input())
answer = ""
max = -1.0
f = []
for i in range(rows):
    f.append(input())

for line in f:
    try:
        if float(line[line.index(" "):]) >= 8.0:
            if max <= float(line[line.index(" "):]):
                max = float(line[line.index(" "):])
                answer = line[:line.index(" ")]
    except:
        continue



if answer == "":
    answer = "Minimum note not reached"
print(answer)
