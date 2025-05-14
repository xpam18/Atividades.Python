nota_trabalho= float(input("Digite sua nota de trabalho: "))
nota_prova= float (input("Digte sua nota de prova: "))
media= (nota_trabalho+nota_prova)/2
print (f"Sua media é: {media:.2f}")
if media >=7:
    print ("APROVADO(A) ")
else:
    print ("REPROVADO(A) ")
    