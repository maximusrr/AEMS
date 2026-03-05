#2. Aprovação de Aluno
#- Solicite a média final de um aluno e exiba o resultado conforme as regras abaixo:
#- Média maior ou igual a 7: Aprovado
#- Média entre 5 e 6,9: Recuperação
#- Média menor que 5: Reprovado

media = float(input("Digite sua média final: "))

if media >= 7:
    print("Aprovado!")

elif media >= 5:
    print("Recuperação!")

else:
    print("Reprovado!")