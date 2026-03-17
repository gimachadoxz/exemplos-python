import os
os.system("cls")

nivel = int(input("Informe o nível do professor (1, 2 ou 3): "))
aulas = int(input("Quantidade de aulas por semana: "))

tabela_precos = {1: 12.00, 2: 17.00, 3: 25.00}

if nivel in tabela_precos:
    valor_hora = tabela_precos[nivel]

    salario = (aulas * valor_hora) * 4
    print(f"\nProfessor Nível {nivel}")
    print(f"Salário Mensal Estimado: R$ {salario:.2f}")
else:
    print("Erro: Nível de professor não reconhecido.")