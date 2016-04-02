import random# biblioteca python para sorteios
import webbrowser# biblioteca python para abrir navegadores
import csv# biblioteca python para ler arquivos csv com lista de convidados
import sys

with open('convidados.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    convidados = []
    for row in reader:
        convidados.append(row['perfil'])

while True:
    print('S para sorteio, P para parar')
    if sys.version_info.major == 3:
        opt = input()
    else:
        opt = raw_input()
    if opt in ['S', 's']:
        ganhador = random.sample(convidados, 1)
        convidados.remove(ganhador[0])
        print(ganhador[0])
        webbrowser.open(ganhador[0])
    else:
        break
