#8. Contador de Números Pares
#Peça ao usuário um número inteiro positivo e exiba todos
# os números pares de 0 até esse número, utilizando um loop while.

num1 = int(input("Digite um valor: "))

contador = 0
while contador <= num1:
    print(contador)
    contador += 2
    print("Fim da contagem. ")