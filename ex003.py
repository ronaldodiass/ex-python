import random

N = int(input("Insira o valor desejado: "))

lista1 = [random.randint(1, 100) for _ in range(N)]
lista2 = [random.randint(1, 100) for _ in range(N)]
lista3 = [random.randint(1, 100) for _ in range(N)]

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista 3:", lista3)

listafinal = []
for i in range(N):
    listafinal.append(lista1[i])
    listafinal.append(lista2[i])
    listafinal.append(lista3[i])

print("Vetor final (intercalado):", listafinal)