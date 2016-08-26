def mundo_pequeno(amigos=[], quantidade=1, origem=(0, 0)):
    minimo = amigos[0]
    for amigo in amigos[1:]:
        if abs(minimo[0] - origem[0]) > abs(amigo[0] - origem[0]):
            minimo = amigo
    if quantidade == 1:
        return {minimo}
    else:
        amigos.remove(minimo)
        r = list(mundo_pequeno(amigos, quantidade - 1, origem))[0]
        minimo = {(minimo)}
        minimo.add(r)
        return minimo
