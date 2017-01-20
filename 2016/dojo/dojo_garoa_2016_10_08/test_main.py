#-*- encoding:utf-8 -*-
"""
A fórmula geral de uma PA é:
an = a1 + (n - 1) * R
Dado um conjunto de números inteiros positivos, identificar todos os subconjuntos de no mínimo 3 elementos onde os números formam uma progressão aritmética.
Devem ser apresentados sempre os maiores subconjuntos que forme uma PA
Por exemplo, dado o subconjunto (1,2,3,5,6,7,9) teríamos como resultado:
(1,2,3)
(5,6,7)
(1,3,5,7,9)
(3,6,9)
(1,5,9)
Note que, por exemplo, (1,3,5) não deve ser apresentada, porque já faz parte de (1,3,5,7,9).
"""


def test_0():
    assert(pa((1, 2)) == False)

def test_1():
    assert(pa((1, 2, 3)) == [(1, 2, 3)])

def test_2():
    assert(pa((1, 2, 3, 4)) == [(1, 2, 3, 4)])

def test_3():
    assert(pa((1, 2, 3, 4, 5, 6)) == [(1, 2, 3, 4, 5, 6)])

def test_4():
    assert(pa((1,2,3,5)) == [(1,2,3),(1,3,5)])

def test_5():
    assert(pa((1,2,3,5,7,9)) == [(1,2,3),(1,3,5,7,9),(1,5,9)])

def pa(n):a
    if type(n) != tuple:
        return False        
    if len(n) < 3:
        return False        
    n = list(n)    
    n.sort()
    n = tuple(n)
   
    for i in range(len(n) - 2):
	R = n[i + 1] - n[i]
        
           
              
              
                


        

#    if (n == (1, 2, 4)):
#        return [(1, 2)]
#    elif (n == (1, 2, 3, 5)):
#        return [(1, 2, 3), (1, 3, 5)]
#    elif (n == (1, 2, 3, 5, 7, 9)):
#        return [(1, 2, 3), (1, 3, 5, 7, 9),(1,5,9)]  
#    else:
#        return [n]

pa(1)
pa((1, 2))
pa((1, 2, 4))
pa((1, 2, 3))
pa((1, 2, 3, 4))
pa((1, 2, 3, 4, 5, 6))
pa((1, 2, 3, 4, 5, 7, 9))
