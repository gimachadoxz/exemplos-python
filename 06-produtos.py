import os
os.system("cls")

produto = input("Descrição do produto: ")
quantidade = int(input(f"Quantidade adquirida de {produto}: "))
preco_unitario = float(input("Preço unitário: R$ "))

total = quantidade * preco_unitario

if quantidade <= 5:
    percentual_desconto = 0.02
elif quantidade <= 10:
    percentual_desconto = 0.03
else:
    percentual_desconto = 0.05

valor_desconto = total * percentual_desconto
total_a_pagar = total - valor_desconto

print("-" * 30)
print(f"Resumo da Compra: {produto}")
print(f"Total Bruto: R$ {total:.2f}")
print(f"Desconto aplicado: {percentual_desconto * 100:.0f}% (R$ {valor_desconto:.2f})")
print(f"Total a Pagar: R$ {total_a_pagar:.2f}")
print("-" * 30)