#9. Sistema de Login Simples
#Solicite nome de usuário e senha.
#Se o usuário for admin e a senha for 1234, exiba:
#Login bem-sucedido!
#Caso contrário, continue solicitando os dados até que estejam corretos.

senha_correta = "1234"
tentativas = 3

while tentativas > 0:
    senha_digitada = input("Digite a senha: ")
    if senha_digitada == senha_correta:
        print("Acesso permitido!")
        break
    else:
        tentativas -= 1
        print("Senha incorreta! Tentativas restantes:", tentativas)

if tentativas == 0:
    print("Tentativas Esgotadas, sistema BLOQUEADO!")