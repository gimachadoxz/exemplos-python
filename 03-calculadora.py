import os
os.system("cls")
numero01 = float(input("Digite o primeiro numero: "))
numero02 = float(input("Digite o segundo numero: "))

print("\nEscolha a operação:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

opcao = input("\nDigite o número da operação (1/2/3/4): ")

if opcao == '1':
    resultado = numero01 + numero02
    print(f"Resultado: {numero01} + {numero02} = {resultado}")
elif opcao == '2':
    resultado = numero01 - numero02
    print(f"Resultado: {numero01} - {numero02} = {resultado}")
elif opcao == '3':
    resultado = numero01 * numero02
    print(f"Resultado: {numero01} * {numero02} = {resultado}")
elif opcao == '4':
    if numero02 != 0:
        resultado = numero01 / numero02
        print(f"Resultado: {numero01} / {numero02} = {resultado}")
    else:
        print("Erro: Não é possível dividir por zero!")
else:
    print("Opção inválida.")