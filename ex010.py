import random

n = int(input("Informe a quantidade N:"))

print("Digite 1 - SIM e 0 - NAO:")

perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]

lista = []
i = 0
while i < n:
  lista_interna = [0,0,0,0,0]
  lista_interna[0] = random.randint(0,1)
  lista_interna[1] = random.randint(0,1)
  lista_interna[2] = random.randint(0,1)
  lista_interna[3] = random.randint(0,1)
  lista_interna[4] = random.randint(0,1)
  lista.append(lista_interna)
  i = i + 1
#print (lista)

i = 0
suspeita = 0
cumplice = 0
assassino = 0
inocente = 0
while i < n:
  soma = sum(lista[i])
  if soma == 2:
    print("Suspeita")
    suspeita += 1
  elif soma == 3 or soma == 4 :
    print("Cumplice")
    cumplice += 1
  elif soma == 5 :
    print("Assassino")
    assassino += 1
  else:
    print("Inocente")
    inocente += 1

  i = i + 1

print("Suspeita ", suspeita)
print("Cumplice ", cumplice)
print("Assassino ", assassino)
print("Inocente ", inocente)