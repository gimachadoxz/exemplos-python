import os
os.system("cls")

Nome = input("Coloque o nome do usuario: ")
senha = input("Coloque a senha do usuario: ")
 
if Nome == "adm" and senha == "123":
    print("Acesso liberado")
   
else:
    print("acesso negado")