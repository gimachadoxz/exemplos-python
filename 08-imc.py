import os
os.system("cls")

peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))

imc = peso / (altura ** 2)

if imc < 16.9:
    situacao = "Muito abaixo do peso"
elif imc <= 18.4:
    situacao = "Abaixo do peso"
elif imc <= 24.9:
    situacao = "Peso normal"
elif imc <= 29.9:
    situacao = "Acima do peso"
elif imc <= 34.9:
    situacao = "Obesidade grau I"
elif imc <= 40:
    situacao = "Obesidade grau II"
else:
    situacao = "Obesidade grau III"

print("-" * 30)
print(f"Seu IMC é: {imc:.2f}")
print(f"Resultado: {situacao}")
print("-" * 30)