#Jogo da forca

#variáveis

palavra_secreta = 'banana'
letras_certas = ['_','_','_','_','_','_']
erros = 0
acertou = False
enforcou = False



print(letras_certas)

while (not acertou and not enforcou):

    chute = input('Qual letra? ')



    if chute in palavra_secreta:

        posicao = 0

        for letra in palavra_secreta:

            if (chute.upper() == letra.upper()):

                print(f'Encontrei a letra \'{letra}\' na posição {posicao}!')
                letras_certas[posicao] = letra
                print(letras_certas)

            posicao += 1

    else:
        erros += 1
        print(f'Não há \'{chute}\' na palavra.')       

    acertou = '_' not in letras_certas
    enforcou = erros == 5


if acertou:
    print('Você ganhou!!!')
else:
    print('Você perdeu :(')