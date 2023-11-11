from funcoes import *
from dics_e_listas import *

print("UrbanFlow Inc. Faça seu cadastro agora mesmo: ")
for key in usuario.keys():
    if type(usuario[key]) is dict:
        for key2 in usuario[key]:
            usuario[key][key2] = input(f"Digite seu/a {key2}: ")
    else:
        usuario[key] = input(f"Digite seu/a {key}: ")
print("Registrado com sucesso! Faça seu login agora mesmo para acessar sua conta: ")
login(usuario)
print(f"Seja bem vindo ao UrbanFlow, {usuario['nome']}!")
while True:
    print("------------------------------------")
    opcao = int(forca_opcao("Qual das opções você deseja realizar? \n"
                  "1 - Exibir todos os ônibus disponíveis agora\n"
                  "2 - Escolher um destino e ver os melhores ônibus para chegar nele\n"
                  "3 - Adicionar um ônibus a minha lista de favoritos\n"
                  "4 - Ver meus ônibus favoritos\n"
                  "5 - Sair\n", opcoes))

    if opcao == 1:
        printar_dic(onibus)
    elif opcao == 2:
        perguntar_destino(destinos, onibus)
    elif opcao == 3:
        opcao_fav = add_fav(onibus, opcoes_fav)
    elif opcao == 4:
        verificar_fav()
    else:
        print("Obrigado por usar o UrbanFlow! Até mais.")
        break

