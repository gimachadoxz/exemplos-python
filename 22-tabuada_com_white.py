import os
os.system("cls")
numero = int(input("Digite um numero:"))
contador = 0 
o_escolhido = int(input("Digite o por até quanto vc quer multiplicar: "))

while(contador <= o_escolhido):
    print(f"{numero} x {contador} = {numero * contador }")
    contador+=1 
 
input("Pressione enter para fechar")