import math
import os

def clear_screen():
    os.system('cls')

def calculo_hipotenusa(cateto1, cateto2):
    hipotenusa = math.sqrt((cateto1**2) + (cateto2**2))
    return hipotenusa

def calculo_cateto(cateto, hipotenusa):
    cateto1 = math.sqrt((hipotenusa**2) - (cateto**2))
    return cateto1

print('Olá! Qual a conta que você deseja fazer?')
opcao = input('Insira H para hipotenusa ou C para cateto: ').upper()

while opcao != 'H' and opcao != 'C':
    print('Esta opção não é válida!')
    opcao = input('Insira H para hipotenusa ou C para cateto: ').upper()

if opcao == 'H':

    clear_screen()

    cateto1 = input('Insira o número do primeiro cateto: ')
    cateto1 = float(cateto1)

    cateto2 = input('Insira o número do segundo cateto: ')
    cateto2 = float(cateto2)

    print(calculo_hipotenusa(cateto1, cateto2))

elif opcao == 'C':

    clear_screen()

    cateto = input ('Insira o número do cateto: ')
    cateto = float(cateto)

    hipotenusa = input('Insira o número da hipotenusa: ')
    hipotenusa = float(hipotenusa)

    print(calculo_cateto(cateto, hipotenusa))
