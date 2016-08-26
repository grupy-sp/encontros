from main import mundo_pequeno


def test_1_mais_proximo():
    amigos = [(1, 0), (2, 0), (3, 0), (4, 0)]
    amigo = mundo_pequeno(amigos, 1)
    assert amigo == {(1, 0)}


def test_2_mais_proximos():
    amigos = [(1, 0), (2, 0), (3, 0), (4, 0)]
    amigo = mundo_pequeno(amigos, 2)
    assert amigo == {(1, 0), (2, 0)}


def test_1_mais_proximo_de_la():
    amigos = [(1, 0), (2, 0), (3, 0), (4, 0)]
    amigo = mundo_pequeno(amigos, 1, (5, 0))
    assert amigo == {(4, 0)}


def test_1_mais_distante():
    amigos = [(1, 0), (2, 0), (3, 0), (4, 0)]
    amigo = mundo_pequeno(amigos, 1, (5, 1))
    assert amigo == {(4, 0)}


def test_outro_mais_distante():
    amigos = [(1, 0), (2, 0), (3, 0), (4, 0)]
    amigo = mundo_pequeno(amigos, 1, (6, 0))
    assert amigo == {(4, 0)}


def test_amigos_mais_10_ainda_em_um_eixo():
    amigos = [(11, 0), (12, 0), (13, 0), (14, 0)]
    amigo = mundo_pequeno(amigos, 1, (6, 0))
    assert amigo == {(11, 0)}
