anoAtual = 2025
anoNascimento = int(input("Digite o seu ano de nascimento: "))
idade = anoAtual-anoNascimento
print(f"Você tem {idade} anos.")
if idade <16:
    print ("Você não pode votar!")
elif idade<18 or idade>70:
    print ("Seu voto é facultativo.")
elif idade>=18:
    print ("Seu voto é obrigatório!")
    