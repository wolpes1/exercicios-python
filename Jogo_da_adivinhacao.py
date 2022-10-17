#jogo de adivinhação


numero_tentativas = 0

while numero_tentativas == 0:
    print ('Bem vindo ao jogo de adivinhação!\nQual você deseja que seja a dificuldade do jogo: ')
    dificuldade = input('Selecione F para Fácil, M para Médio e D para Difícil:')

    dif_facil = dificuldade.upper() == "F"
    dif_medio = dificuldade.upper() == "M"
    dif_dificil = dificuldade.upper() == "D"


    if (dif_facil):
        numero_tentativas = 7
    elif (dif_medio):
        numero_tentativas = 5
    elif (dif_dificil):
        numero_tentativas = 3
    else:
        print('\nTente novamente\n')
        



adivinhacao = 7

while numero_tentativas != 0:

    numero_tentativas -= 1
    
    print('\nTente adivinhar o número oculto:')
    tentativa = input('Digite um número de 0 a 10: \n')
    tentativa = int(tentativa)

    acerto = tentativa == adivinhacao
    maior = tentativa > adivinhacao
    menor = tentativa < adivinhacao

    mensagem_acerto = '\nVocê acertou!\nParabéns!'
    mensagem_maior = (f'\nO número chutado {tentativa} foi maior que o número da adivinhação!')
    mensagem_menor = (f'\nO número chutado {tentativa} foi menor que o número da adivinhação!')
    msg_nova_tentativa = ('\nTente de novo!')
    msg_sem_tentativa = ('\nAcabaram as tentativas :(\n')

    tentativa_final = numero_tentativas == 0

    if (tentativa_final):
        if (acerto):
            print (mensagem_acerto)
        elif (maior):
            print (mensagem_maior)
            print (msg_sem_tentativa)
        elif (menor):
            print (mensagem_menor)
            print (msg_sem_tentativa)
    else:
        if (acerto):
            print (mensagem_acerto)
            break
        elif (maior):
            print (mensagem_maior)
            print (msg_nova_tentativa)
        elif (menor):
            print (mensagem_menor)
            print (msg_nova_tentativa)