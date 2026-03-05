#3. Verificação de Idade para Dirigir
#- Peça ao usuário sua idade e informe se ele pode tirar a carteira de motorista.
#- Idade mínima exigida: 18 anos.

idade = float(input("Digite sua idade: "))

if idade >= 18:
    print("Permitido. Você pode tirar sua CNH.")

else:
    print("Não permitido. Você não possui idade para retirar sua CNH.")