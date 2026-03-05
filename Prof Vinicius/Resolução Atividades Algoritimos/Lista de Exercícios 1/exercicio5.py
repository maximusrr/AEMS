#5. Verificador de Ano Bissexto
#Peça ao usuário um ano e informe se ele é bissexto ou não.
#Um ano é bissexto quando:
#É divisível por 4,
#Não é divisível por 100,
#Exceto se for divisível por 400.

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print ("Seu ano é Bissexto.")
else:
    print("Seu ano não é Bissexto.")