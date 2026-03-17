import random
 
numero_secreto = random.randint(1, 10)
 
palpite = int(input("Tente adivinhar o número (entre 1 e 10): "))
 
if palpite == numero_secreto:
    print("Acertou!")
else:
    print("Errou! O número era:", numero_secreto)