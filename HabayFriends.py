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


ms = set(signedYes)
signedYes = list(ms)
signedYes.sort()
signedNo.sort()


for y in signedYes:
    print(y[:y.index(" YES")])

for y in signedNo:
    print(y[:y.index(" NO")])

print("")

print("Amigo do Habay:\n" + habayFriend[:habayFriend.index("YES")])