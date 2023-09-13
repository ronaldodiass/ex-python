
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

print(f"A média anual das temperaturas é: {media_anual:.2f}°C")
if meses_acima_media:
    print("Mes com temperaturas acima da média anual:")
    for mes in meses_acima_media:
        print(mes)
else:
    print("Não houve meses com temperaturas acima da média anual.")