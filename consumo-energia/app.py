# Entrada

aparelho = input("Qual o nome do aparelho? ")
potencia_w = float(input("Qual a potência desse aparelho? "))
tempo_medio = int(input("Qual o tempo médio por dia de uso do aparelho? "))
custo_kwh = float(input("Qual o valor do kWh na sua região (em R$)?"))

# Processamento

consumo_mensal = (potencia_w * tempo_medio * 30) / 1000
gasto_consumo = consumo_mensal * custo_kwh

# Saída

print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f}kWh/mês")
print(f"O gasto mensal estimado é: R$ {gasto_consumo:.2f}")


