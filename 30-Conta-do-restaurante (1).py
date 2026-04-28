import os
os.system("cls")

def valor_por_pessoa(valor_conta, quantidade_pessoas):
    valor_por_pessoa = valor_conta / quantidade_pessoas
    return valor_por_pessoa
print("Seja bem vindo ao app minha conta!")

 
valor_da_conta = int(input("Informe o valor total da conta: "))
numero_de_pessoas = int(input("Iforme o numero total de pessoas:"))
#chamando a função
resultado_final = valor_por_pessoa(valor_da_conta, numero_de_pessoas)

#Exibindo os resultados formatados
print(f"Total da conta: R$ {valor_da_conta:.2f}")
print(f"Número de Pessoas: {numero_de_pessoas}")
print(f"Valor por pessoa: R$ {resultado_final:.9f}")

print(f"Fim do programa!")