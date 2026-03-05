#6. Classificação por Idade
#Peça a idade do usuário e classifique conforme as categorias abaixo:
#Menor de idade: menos de 18 anos
#Adulto: entre 18 e 60 anos
#Idoso: mais de 60 anos

idade = int(input("Digite sua idade: "))

if idade <18:
    print("Você é menor de idade.")
elif idade <= 60:
    print("Você é adulto.")
else:
    print("Você é idoso.")