habayFriend = ""
signedList = []
signedYes = []
signedNo = []
s = ""

while s != "FIM":
    s = input()
    signedList.append(s)


for s in signedList:
    if "YES" in s:
        signedYes.append(s)
        if len(habayFriend) < len(s):
            habayFriend = s
    elif "NO" in s:
        signedNo.append(s)

print('Saída')
ms = set(signedYes)
signedYes = list(ms)
signedYes.sort()
signedNo.sort()
signedList.clear()
signedList = signedYes + signedNo

for y in signedList:
    print(y[:y.index("YES"  if "YES" in y else "NO")])

print("Amigo do Habay: \n", habayFriend[:habayFriend.index("YES")])