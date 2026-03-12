from datetime import datetime

# 1. ENTRADA DE DADOS
qtd_sup = int(input("Quantidade de Supervisores: "))
qtd_mon = int(input("Quantidade de Montadores: "))

inicio_str = input("Horário de Início (HH:MM): ")
fim_str = input("Horário de Fim (HH:MM): ")

# 2. CÁLCULO DO TEMPO (Transformando em Decimal)
formato = "%H:%M"
h1 = datetime.strptime(inicio_str, formato)
h2 = datetime.strptime(fim_str, formato)
diferenca = h2 - h1

minutos = diferenca.seconds / 60
decimal = minutos / 60

# 3. CÁLCULO SEPARADO POR CATEGORIA
total_sup = qtd_sup * decimal
total_mon = qtd_mon * decimal

# 4. EXIBIÇÃO DOS RESULTADOS
print("-" * 30)
print(f"Tempo decorrido: {int(minutos)} min ({decimal:.2f} em decimal)")
print("-" * 30)
print(f"RESULTADO SUPERVISORES: {total_sup:.2f} horas/homem")
print(f"RESULTADO MONTADORES: {total_mon:.2f} horas/homem")
print("-" * 30)
print(f"TOTAL GERAL DA EQUIPE: {(total_sup + total_mon):.2f} horas/homem")