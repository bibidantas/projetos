# Calculadora-de-consumo-de-energia
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Energia](https://img.shields.io/badge/tema-energia-orange)

**Projeto feito em _Python_, criado com o objetivo de realizar o cálculo de gastos com aparelhos eletrônicos domésticos, facilitando a organização de contas e ajudando na economia de energia.**

## 🌐 Linguagem usada: <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40"/>

## 🧠 Como funciona

O programa segue o fluxo:

**Entrada → Processamento → Saída**

1. O usuário informa:
- Nome do aparelho  
- Potência (em watts)  
- Tempo médio de uso diário (em horas)  
- Valor do kWh (R$)  

2. O sistema realiza os cálculos de:
- Consumo mensal (kWh)  
- Gasto mensal estimado (R$)  

3. Os resultados são exibidos de forma clara no terminal.
## 💻 Código principal

* Entrada
```
aparelho = input("Qual o nome do aparelho? ")

potencia_w = float(input("Qual a potência desse aparelho? "))

tempo_medio = int(input("Qual o tempo médio por dia de uso do aparelho? "))
```
* Processamento
```
consumo_mensal = (potencia_w * tempo_medio * 30) / 1000
```
* Saída
```
print(f"Aparelho: {aparelho}")

print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
```

## ▶️ Como executar

1. Tenha o Python instalado
2. Abra o VS Code <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" width="30"/>
3. Execute o arquivo:
_python app.py_
4. Insira os dados solicitados:
* Nome do aparelho
* Potência (W)
* Tempo de uso diário (horas)
* Valor do kWh (R$)

## 📊 Exemplo de uso
```
Qual o nome do aparelho? Geladeira

Qual a potência desse aparelho? 150

Qual o tempo médio por dia de uso do aparelho? 24

Aparelho: Geladeira

Consumo estimado: 108.00 kWh/mês
```
## 🎯 Objetivos do projeto
- Praticar lógica de programação em Python
- Trabalhar com entrada, processamento e saída de dados
- Aplicar cálculos simples no mundo real

## 🚀 Possíveis melhorias
- Permitir múltiplos aparelhos
- Criar interface gráfica
- Exportar resultados

##

### Sinta-se à vontade para contribuir com melhorias ou sugestões! ♡
