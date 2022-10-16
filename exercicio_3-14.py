#jogo de adivinhação

numero_tentativas = 3

adivinhacao = 7

while numero_tentativas != 0:

    numero_tentativas -= 1
    
    print('Tente adivinhar o número oculto:')
    tentativa = input('Digite um número de 0 a 10: ')
    tentativa = int(tentativa)

    acerto = tentativa == adivinhacao
    maior = tentativa > adivinhacao
    menor = tentativa < adivinhacao

    mensagem_acerto = 'Você acertou!\nParabéns!'
    mensagem_maior = (f'O número chutado {tentativa} foi maior que o número da adivinhação!')
    mensagem_menor = (f'O número chutado {tentativa} foi menor que o número da adivinhação!')
    msg_nova_tentativa = ('Tente de novo!')
    msg_sem_tentativa = ('Acabaram as tentativas :(')

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