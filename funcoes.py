import json
import pandas as pd

def forca_opcao(msg, lista):
    x = input(msg)
    if x not in lista:
        print("Digite uma opção cadastrada!")
        return forca_opcao(msg, lista)
    return x

def login(dic_usuario):
    email_login = input("Digite seu email: ")
    senha_login = input("Digite sua senha: ")
    i = 3
    while i > 0:
        if email_login != dic_usuario['email'] or senha_login != dic_usuario['senha']:
            if i == 1:
                print("Seu número de tentativas acabou! Tente novamente mais tarde.")
                quit()
            i -= 1
            print(f"Email ou senha incorretos! Mais {i} tentativas!")
            email_login = input("Digite seu email: ")
            senha_login = input("Digite sua senha: ")
            continue
        else:
            break
    return


def printar_dic(dic):
    print(pd.DataFrame(dic))
    return


def perguntar_destino(lista, dic):
    for i in range(len(lista)):
        print(f"{i} : {lista[i]}")
    destino = int(forca_opcao("Para qual destino você quer ir? ", ['0', '1', '2']))
    if destino == 0:
        for i in range(3):
            print(f"----- OPÇÃO {i + 1} -----")
            for key in dic.keys():
                print(f"{key} : {dic[key][i]}")
    elif destino == 1:
        for i in range(3, 6):
            print(f"----- OPÇÃO {i - 2} -----")
            for key in dic.keys():
                print(f"{key} : {dic[key][i]}")
    else:
        for i in range(6, 9):
            print(f"----- OPÇÃO {i - 5} -----")
            for key in dic.keys():
                print(f"{key} : {dic[key][i]}")
    return


def carregar_favoritos():
    nome_arquivo = "favoritos.json"
    try:
        with open(nome_arquivo, "r") as arquivo:
            return json.load(arquivo)
    except json.decoder.JSONDecodeError:
        return {"números": [], "nomes": []}
    except FileNotFoundError:
        return {"números": [], "nomes": []}


def salvar_favoritos(favoritos):
    nome_arquivo = "favoritos.json"
    with open(nome_arquivo, "w") as arquivo:
        json.dump(favoritos, arquivo, ensure_ascii=False)


def add_fav(dic_onibus, opcoes_fav):
    favoritos = carregar_favoritos()
    for i in range(len(dic_onibus['nome'])):
        print(f"{i} : {dic_onibus['número'][i]} - {dic_onibus['nome'][i]}")

    opcao_fav = int(forca_opcao("Qual ônibus você deseja adicionar aos seus favoritos? ", opcoes_fav))

    numero = dic_onibus['número'][opcao_fav]
    nome = dic_onibus['nome'][opcao_fav]

    if numero in favoritos["números"]:
        print("Esse ônibus já está na lista de favoritos! Escolha outro.")
    else:
        favoritos["números"].append(numero)
        favoritos["nomes"].append(nome)
        print(f"Ônibus {dic_onibus['número'][opcao_fav]} - {dic_onibus['nome'][opcao_fav]} adicionado com sucesso!")
        salvar_favoritos(favoritos)

    return opcao_fav

def verificar_fav():
    try:
        with open('favoritos.json', 'r') as ler:
            dic_ler = json.load(ler)
            print("Lista de Favoritos: ")
            for i in range(len(dic_ler['nomes'])):
                print(f"{dic_ler['números'][i]} - {dic_ler['nomes'][i]}")
    except FileNotFoundError:
        print("Você não tem favoritos!")
    except json.decoder.JSONDecodeError:
        print("Você não tem favoritos!")
    return