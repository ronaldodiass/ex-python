def calcular_media(valores):
    if not valores:
        return 0
    return sum(valores) / len(valores)

temperaturas_mensais = []

meses = {
    1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
    5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
    9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
}

for mes in range(1, 13):
    temperatura = float(input(f"Digite a temperatura média de {meses[mes]}: "))
    temperaturas_mensais.append(temperatura)

media_anual = calcular_media(temperaturas_mensais)

meses_acima_media = [meses[i] for i, temperatura in enumerate(temperaturas_mensais, start=1) if temperatura > media_anual]

resultados = {
    "Media Anual": f"{media_anual:.2f}°C",
    "Meses Acima da Média Anual": meses_acima_media
}

print("Resultados:")
for chave, valor in resultados.items():
    print(f"{chave}: {valor}")

with open("resultados.txt", "w") as arquivo:
    arquivo.write("Resultados:\n")
    for chave, valor in resultados.items():
        arquivo.write(f"{chave}: {valor}\n")

print("Resultados salvos no arquivo 'resultados.txt'.")