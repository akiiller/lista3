pares = []
impares = []
entradas = []
linhas = int(input())

for i in range(0, linhas):
    entradas.append(int(input()))
    if entradas[i] % 2 == 0:
        pares.append(entradas[i])
    else:
        impares.append(entradas[i])

pares.sort()
impares.sort(reverse=True)

for par in pares:
    print(par)

for impar in impares:
    print(impar)



