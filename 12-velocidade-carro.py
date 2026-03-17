import os
os.system("cls")

ano = float(input("Coloque o ano: "))
 
if ano % 4 == 0:
    print("ano bissexto")
 
else:
    print("não é bissexto")