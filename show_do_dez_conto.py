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

def perdeu():
    clear_screen()
    print('Você perdeu :(')
    input('Pressione enter para sair.')

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

def responder_pergunta(resposta_certa):
    opcao_escolhida = input('Escolha sua opção: ')
    return analizar_resposta_jogo(opcao_escolhida, resposta_certa)

# Perguntas

def pergunta_1():
    clear_screen()
    print('Vamos à primeira pergunta!\nQual foi o local em que ocorreram as Olimpíadas de 2008?')
    print('A) África do Sul\nB) Pequim\nC) Rússia\nD) Brasil')

def pergunta_2():
    clear_screen()
    print('Vamos à segunda pergunta!\nEm que ano começou a Segunda Guerra Mundial?')
    print('A) 1896\nB) 1930\nC) 1937\nD) 1945')

def pergunta_3():
    clear_screen()
    print('Vamos à terceira pergunta!\nQual foi o poema mais famoso de Edgar Allan Poe?')
    print('A) O Corvo\nB) Anabelle\nC) O Cortiço\nD) Acalanto')

def pergunta_4():
    clear_screen()
    print('Vamos à quarta pergunta!\nNo anime Demon Slayer (Kimetsu no Yaiba), como é o nome da irmã Oni de Tanjiro?')
    print('A) Ishikawa\nB) Kirino\nC) Nezuko\nD) Hikaru')

def pergunta_5():
    clear_screen()
    print('Vamos à quinta pergunta!\nEm biologia, qual é o nome científico dos sapos?')
    print('A) Lupus\nB) Canis\nC) Mustela\nD) Rhinella')

def pergunta_6():
    clear_screen()
    print('Vamos à sexta pergunta!\nNos anos 1996, a Nintendo havia recém lançado o seu video-game. Qual era?')
    print('A) GameCube\nB) GameBoy Advance\nC) Nintendo 64\nD) Nintendo DS')

def pergunta_7():
    clear_screen()
    print('Vamos à sétima pergunta!\nQual destas músicas é pertencente à banda Queen?')
    print('A) Paint It, Black\nB) Hammer to Fall\nC) Californication\nD) Livin\' on a prayer')

def pergunta_8():
    clear_screen()
    print('Vamos à oitava pergunta!\nQual destes remédios serve para o tratamento de ansiedade?')
    print('A) Sertralina\nB) Dipirona\nC) Fentanil\nD) Omeprazol')

def pergunta_9():
    clear_screen()
    print('Vamos à nona pergunta!\nQuando o delta é positivo no Teorema de Bháskara, quanto é o máximo de respostas possíveis?')
    print('A) 0\nB) Inexistente\nC) 1\nD) 2')

def pergunta_10():
    clear_screen()
    print('Vamos à pergunta dos dez conto!\nEm qual frase há o uso correto da crase?')
    print('A) Veja às horas\nB) Bem vindos à Buenos Aires\nC) Receba quem estiver à porta\nD) Vamos jogar à bola?')

# Funcionamento Menu

print(mensagem_intro)
escolha_jogador = input(menu_escolha_intro)
escolha_certa = analizar_resposta_menu(escolha_jogador, "A", "B")


if escolha_certa.upper() == "B":
    input(agradecimentos)
else:
    # Começa o jogo

    correcao = True
    while correcao == True:

        pergunta_1()
        correcao = responder_pergunta('B')
        if correcao == False:
            perdeu()
            break
        
        correcao = None
        pergunta_2()
        correcao = responder_pergunta('D')
        if correcao == False:
            perdeu()
            break

        correcao = None
        pergunta_3()
        correcao = responder_pergunta('A')
        if correcao == False:
            perdeu()
            break

        correcao = None
        pergunta_4()
        correcao = responder_pergunta('C')
        if correcao == False:
            perdeu()
            break
        
        correcao = None
        pergunta_5()
        correcao = responder_pergunta('D')
        if correcao == False:
            perdeu()
            break
        
        correcao = None
        pergunta_6()
        correcao = responder_pergunta('C')
        if correcao == False:
            perdeu()
            break

        correcao = None
        pergunta_7()
        correcao = responder_pergunta('B')
        if correcao == False:
            perdeu()
            break

        correcao = None
        pergunta_8()
        correcao = responder_pergunta('A')
        if correcao == False:
            perdeu()
            break

        correcao = None
        pergunta_9()
        correcao = responder_pergunta('D')
        if correcao == False:
            perdeu()
            break

        correcao = None
        pergunta_10()
        correcao = responder_pergunta('C')
        if correcao == False:
            perdeu()
            break

        clear_screen()
        input(ganhador)
        break