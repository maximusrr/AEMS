#4. Desconto em Compras
#- Solicite o valor de uma compra.
#- Se o valor for maior que R$ 100, aplique um desconto de 10% e exiba o valor final com desconto.
#- Caso contrário, o preço permanece o mesmo.

valor = float(input("Digite o valor da compra: "))

if valor > 100:
    desconto = valor * 0.10
    valorfinal = valor - desconto
    print("Seu valor com desconto é de:", valorfinal)

else:
    print("Você não possui desconto!","Valor final:", valor)