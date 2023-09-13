import random

N = int(input("Insira o valor desejado: "))

lista = [random.randint(1, 100) for _ in range(N)]

print("Lista: ", lista)

soma = sum(x ** 2 for x in lista)

print("Soma dos quadrados dos elementos da lista:", soma)