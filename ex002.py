import random

N = int(input("Insira o valor desejado: "))

lista1 = [random.randint(1, 100) for _ in range(N)]
lista2 = [random.randint(1, 100) for _ in range(N)]

print("Lista 1:", lista1)
print("Lista 2:", lista2)

lista3 = []
for i in range(N):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print("Lista 3 (intercalado):", lista3)