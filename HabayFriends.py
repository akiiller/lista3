habayFriend = ""
signedList = []
signedYes = []
s = ""

while s != "FIM":
    s = input()
    signedList.append(s)


for s in signedList:
    if "YES" in s:
        signedYes.append(s)
        if len(habayFriend) < len(s):
            habayFriend = s

print('Saída')
ms = set(signedYes)
signedYes = list(ms)
signedYes.sort()

for y in signedYes:
    print(y[:y.index("YES")])

print("Amigo do Habay: \n", habayFriend[:habayFriend.index("YES")])