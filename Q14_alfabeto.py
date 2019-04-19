

"""Escreva um programa que verifica se todas as letras do alfabeto constam no mínimo uma
vez do parágrafo fornecido pelo usuário."""

from string import ascii_letters

def paragrafo(par):
    for each in ascii_letters:
        if each in par:
            continue
        else:
            return False
    return True


if __name__ == '__main__':
    frase = str(input('Entre com um texto digitado entre aspas:',))
    #A frase abaixo contém todas as letras, serve para teste da resposta True
    #frase = 'à noite, vovô Kowalsky vê o ímã cair no pé do pingüim queixoso e vovó põe açúcar no chá de tâmaras do jabuti feliz'
    print('O texto contém todas as letras do alfabeto?', paragrafo(frase))


#Tem que adicionar uma solução para que o texto leia mais de uma linha


