#Classificação de IMC
#Peça ao usuário que informe:
#Peso (em kg)
#Altura (em metros)
#Calcule o IMC usando a fórmula:
##IMC = peso / (altura × altura)
#Classifique conforme as faixas:
#Abaixo de 18,5: Abaixo do peso
#Entre 18,5 e 24,9: Peso normal
#Entre 25 e 29,9: Sobrepeso
#30 ou mais: Obesidade

peso = float(input("Digite seu peso(KG): "))
altura = float(input("Digite sua altura(m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Seu IMC é de: {imc}. Você está abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print(f"Seu IMC é de: {imc}. Você está com o peso normal.")