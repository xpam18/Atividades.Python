import random 
numero_secreto = random.randint (1,10)
tentativas = 0 
contagem_tentativas = 0
print ("***BEM-VINDO AO JOGO DA ADIVINHÇÃO***")
print ("Tente adivinhar o número secreto entre 1 e 10 ")
while tentativas != numero_secreto:
    numero = int(input ("Digite um número: "))
    contagem_tentativas = contagem_tentativas+1
    if numero == numero_secreto:
        print ("VOCÊ ACERTOU!!!")
        print (f"VOCÊ PRECISOU DE {contagem_tentativas}")
        break
    elif numero< numero_secreto:
        print ("O NÚMERO SECRETO É MAIOR. ")
    else:
        print ("O NÚMERO SECRETO É MENOR. ")
