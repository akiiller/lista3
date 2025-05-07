n, q = input().split()

notes = []
queries = []

for i in range(int(n)):
    notes.append(int(input()))

sorted_notes = notes.sort()
print(notes)

for p in range(int(q)):
    queries.append(int(input()))

for o in range(len(queries) ):
    print(notes[queries[o] -1 ])