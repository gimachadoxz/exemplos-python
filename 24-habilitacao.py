import os
os.system("cls")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura (ex: 1.70): "))
deficiencia = input("Tem alguma deficiência? (sim/nao): ").lower()
carteira = input("Você já tem carteira? (sim/nao): ").lower()
alcool = input("Você ingeriu álcool? (sim/nao): ").lower()

print("\nTipos de veículo:")
print("1 - Carro")
print("2 - Moto")
print("3 - Caminhão")

veiculo = input("Escolha o tipo de veículo (1/2/3): ")

print("\n--- RESULTADO ---\n")

if idade < 18:
    print(f"{nome}, você não pode dirigir: menor de idade.")

elif carteira != "sim":
    print(f"{nome}, você não pode dirigir: sem carteira.")

elif alcool == "sim":
    print(f"{nome}, você não pode dirigir: álcool e direção não combinam.")

else:

    if veiculo == "1":  
        if altura < 1.40:
            print(f"{nome}, você é muito baixo para dirigir carro com segurança.")
        else:
            print(f"{nome}, você pode dirigir carro ")

    elif veiculo == "2":  
        if altura < 1.50:
            print(f"{nome}, você não tem altura suficiente para dirigir moto.")
        else:
            print(f"{nome}, você pode dirigir moto ")

    elif veiculo == "3":  
        if altura < 1.60:
            print(f"{nome}, você não tem altura suficiente para dirigir caminhão.")
        else:
            print(f"{nome}, você pode dirigir caminhão ")

    else:
        print("Tipo de veículo inválido.")

    
    if deficiencia == "sim":
        print("Obs: é necessário avaliação médica e CNH especial.")