#1. Verificação de Maior Número 
#- Peça ao usuário para digitar dois números e informe qual é o maior.
#- Caso os dois números sejam iguais, informe que eles são iguais.

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))

if numero1 > numero2:
    print("O maior número é: ", numero1)

elif numero2 > numero1:
    print("O maior número é: ", numero2)

else:
    print("Os dois números são Iguais.")