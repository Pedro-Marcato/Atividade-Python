#Turma:ADSDM2CB
#Participantes: 
#Pedro Araújo Marcato, 2324291026
#Carlos Eduardo Moura Abe, 2324291011

Vendas = {}
N = int(input("Em quantos dias da semana houve vendas: "))

for i in range (N):
    dia = input("Dia da semana: ")
    venda = int(input("Quantidade de vendas: "))
    Vendas[dia] = venda

Total = sum(Vendas.values())
Maior = max(Vendas.values())
Menor = min(Vendas.values())
Media = Total / N
Acima = [dia for dia, venda in Vendas.items() if venda > Media]

print(f"\n {Vendas} \n")

print(f"Total de vendas: {Total}")
print(f"Maior venda: {Maior}")
print(f"Menor venda: {Menor}")
print(f"Media: {Media}")
print(f"Dias acima da media: {Acima}")