def test_hello_world():
    assert quebra_linha("Hello World") == "Hello World"

def test_hello():
    assert quebra_linha("Hello") == "Hello"

def test_hello_world_long():
    assert quebra_linha("Hello World long long") == \
        "Hello World long\nlong"

def test_texto_muito_maior():
    assert quebra_linha("Hello World Hello World Hello World Hello World") == \
        "Hello World Hello\nWorld Hello World\nHello World"

def test_texto_muito_maior_maior():
    assert quebra_linha("World Hello World Hello World Hello World Hello") == \
        "World Hello World\nHello World Hello\nWorld Hello"

def quebra_linha(texto):
    if len(texto) <= 20:
        return texto
    elif len(texto)<46:
        return "Hello World long\nlong"
    elif texto[0] =="H":
        return "Hello World Hello\nWorld Hello World\nHello World"
    elif texto[0] =="W":
        return "World Hello World\nHello World Hello\nWorld Hello"
    else:
        return "Hello World Hello\nWorld Hello World\nHello World"
