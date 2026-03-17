import os
os.system("cls")

print("Selecione o tipo de veículo:")
print("1 - Carro")
print("2 - Moto")
print("3 - Caminhão")
 
opcao = input("Digite o número da opção: ")
 
if opcao == "1":
    print("O valor do pedágio para Carro é: R$ 10,00")
elif opcao == "2":
    print("O valor do pedágio para Moto é: R$ 5,00")
elif opcao == "3":
    print("O valor do pedágio para Caminhão é: R$ 20,00")
else:
    print("Tipo inválido")