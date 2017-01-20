# -*- coding: utf-8 -*-
"""
Um número primo é definido se ele possuir exatamente dois divisores: o número um e ele próprio. São exemplos de números primos: 2, 3, 5, 101, 367 e 523.
Neste problema, você deve ler uma palavra composta somente por letras [a-zA-Z]. Cada letra possui um valor específico, a vale 1, b vale 2 e assim por diante, até a letra z que vale 26. Do mesmo modo A vale 27, B vale 28, até a letra Z que vale 52.
Você precisa definir se cada palavra em um conjunto de palavras é prima ou não. Para ela ser prima, a soma dos valores de suas letras deve ser um número primo.

>>> palavra_prima('b')
True
>>> palavra_prima('d')
False
>>> palavra_prima('C')
True
>>> palavra_prima('B')
False
>>> palavra_prima('grupy')
False
>>> palavra_prima('aaaa')
False
>>> palavra_prima('aaa')
True
>>> palavra_prima('a')
False
>>> palavra_prima('CB')
False
>>> palavra_prima('G')
False
>>> soma_palavra('A')
27
>>> soma_palavra('aaaa')
4



"""
import string

#print(letras)
#letras = [ord(str(x) for x in range(97, 123)]

#print(letras)
def palavra_prima(palavra):
    import math
    soma = soma_palavra(palavra)
    if soma == 1:
        return False

    for i in range(2, int(math.sqrt(soma))+1):
        if soma%i == 0:
            return False

    return True

def retorna_numero(letra):
    lista = list(string.ascii_letters)
    indice = lista.index(letra) + 1

    return indice

def soma_palavra(palavra):

    soma = int()
    for letra in palavra:
        soma += retorna_numero(letra)
    return soma
