# Definição: Um jogo com 10 perguntas, onde caso hajam 10 acertos, o ganhador ganhará 10 reais. Mas caso erre, perderá tudo.

# Requisitos: Sistema de Menu, Sistema de Perguntas e Respostas

import os

def clear_screen():
    os.system('cls')

# Definições Menu

mensagem_intro = 'Bem vinds ao\n******************************\n******Show Dos Dez Conto******\n******************************'
menu_escolha_intro = 'O que você deseja fazer? A)Jogar ou B)Sair?\n'
erro_escolha = 'Esta não é uma opção! Por favor, escolha entre as duas letras maiores (A ou B).\n'
agradecimentos = 'Obrigado por jogar conosco!\nPressione enter para sair.'
ganhador = 'Parabéns, você ganhou os dez conto!\nPressione enter para sair.'

# Funções

def analizar_resposta_menu(resposta,resposta_correta_1,resposta_correta_2):
    while resposta.upper() != resposta_correta_1 and resposta.upper() != resposta_correta_2:
        clear_screen()
        print(erro_escolha)
        resposta = input(menu_escolha_intro).upper()
        clear_screen()
    return resposta

def analizar_resposta_jogo(resposta,resposta_correta):
    if resposta.upper() == resposta_correta.upper():
        return True
    else:
        return False


# Perguntas jogo

def pergunta_1():
    print('Vamos à primeira pergunta!\nQual foi o local em que ocorreram as Olimpíadas de 2008?')
    print('A) África do Sul\nB) Pequim\nC) Rússia\nD) Brasil')

# Funcionamento Menu

print(mensagem_intro)
escolha_jogador = input(menu_escolha_intro)
escolha_certa = analizar_resposta_menu(escolha_jogador, "A", "B")


if escolha_certa == "B":
    input(agradecimentos)
else:
    # Começa o jogo

    correcao = True
    while correcao == True:

        pergunta_1()
        opcao_escolhida = input('Escolha sua opção: ')
        correcao = analizar_resposta_jogo(opcao_escolhida, 'B')
        if correcao == False:
            break
        
        clear_screen()
        input(ganhador)
        break






