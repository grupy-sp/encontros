# File: test_soma.py
# Comando: py.test

unidade = ['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis','sete','oito','nove', 'dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove']
dezenas = ['dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta','oitenta', 'noventa']

def centavos(valor):
    cents = (valor - int(valor) ) * 100
    if cents == 1:
        return "um centavo"
    if cents > 0 and cents < 20:
        return unidade[int(cents)] + " centavos"
    if cents >= 20:
        uni = cents % 10
        return  unidade[int(uni)] + " centavos"
    else:
        return ''

def extenso(valor):
    if valor == 200:
        return "duzentos reais"
    elif valor == 1:
        return "um real"
    elif valor == 2:
        return "dois reais"
    return "cem reais e cinco centavos"


def test_extenso():
    assert extenso(200.00) == "duzentos reais"
    assert extenso(100.05) == "cem reais e cinco centavos"
    assert extenso(1.00) == "um real"
    assert extenso(2.00) == "dois reais"
    assert centavos(00.11) == 'onze centavos'
    assert centavos(00.02) == "dois centavos"
    assert centavos(00.07) == "sete centavos"
    assert centavos(00.12) == "doze centavos"
    assert centavos(20.00) == ""
    assert centavos(00.90) == "noventa centavos"
