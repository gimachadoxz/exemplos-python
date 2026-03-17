import os
os.system("cls")

horas = float(input("Coloque quantas horas você passou no dia estudando: "))
 
if horas <2:
    print("pouco tempo")
 
if horas >=2 and horas <= 4:
    print("Estudo medio")
 
if horas >4:
    print("muito tempo")