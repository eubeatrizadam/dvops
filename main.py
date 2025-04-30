import random
from time import sleep

print("\n ZOMBIE DICE \n")
print("Seja bem-vindo ao jogo Zombie Dice!\n")

#Dados dos Jogadores, limite de pessoas definido 2+
numJogadores = 0

while (numJogadores < 2):
    numJogadores = int(input("Informe a quantidade de jogadores: "))
    print("O total de jogadores é {}".format (numJogadores))

    if (numJogadores < 2):
        print("AVISO: Você precisa de pelo menos 2 jogadores!")

listaJogadores = []

for c in range (0, numJogadores):
    nome = input(f'Digite o nome do {c + 1}º jogador: ').upper()
    listaJogadores.append(nome)

def dadoVerde():
    dadoVerde = ("C", "P", "C", "T", "P", "C")
    return dadoVerde

def dadoAmarelo():
    dadoAmarelo = ("T", "P", "C", "T", "P", "C")
    return dadoAmarelo

def dadoVermelho():
    dadoVermelho = ("T", "P", "T", "C", "P", "T")
    return dadoVermelho

listaDados = [
    dadoVerde(), dadoVerde(), dadoVerde(), dadoVerde(), dadoVerde(), dadoVerde(),
    dadoAmarelo(), dadoAmarelo(), dadoAmarelo(), dadoAmarelo(),
    dadoVermelho(), dadoVermelho(), dadoVermelho()
]
    # Lista de dados previamente estipulada pelo enunciado da questão


print("\nIniciando o jogo!\n")

jogadorAtual = 0
dadosSorteados = []
tiros = 0
cerebros = 0
passos = 0
pontos = []

#contador de pontos
for i in range(0, numJogadores):
    pontos.append(0)
#sorteador de dados
def sorteamentoDados (corDado = ()):
    for n in range (0, 3):
        numSorteado = random.randrange(13)
        dadoSorteado = listaDados[numSorteado]
        if dadoSorteado == dadoVerde():
            corDado = "VERDE"
        elif dadoSorteado == dadoAmarelo():
            corDado = "AMARELO"
        elif dadoSorteado == dadoVermelho():
            corDado = "VERMELHO"

        print("O dado sorteado foi", corDado)
        dadosSorteados.append(dadoSorteado)
        sleep(1)

while True:

    print('Turno do jogador: ', listaJogadores[jogadorAtual])

    sorteamentoDados()
#sorteio das faces
    for dadoSorteado in dadosSorteados:
        numFaces = random.randint(0, 5)
        if dadoSorteado[numFaces] == "C":
            print('Você comeu um CÉREBRO!')
            cerebros += 1

        elif dadoSorteado[numFaces] == "T":
            print('Você levou um TIRO!')
            tiros += 1

        else:
            print('Você tirou um PASSO! Sua vítima escapou!')
            passos += 1
    sleep(1)

    print("\n===SCORE ATUAL===")
    print("CÉREBROS: ", cerebros)
    print("PASSOS - ", passos)
    print("TIROS: ", tiros)

# Soma a quantidade de passos, tiros e score do jogador

    if tiros > 2:
        print('Você perdeu essa rodada! Levou, ', tiros, ' tiros\n')
        tiros = 0
        cerebros = 0
        passos = 0
        dadosSorteados = []
        jogadorAtual += 1

        if jogadorAtual == len(listaJogadores):
            jogadorAtual = 0
            print('Indo para a próxima rodada, jogador: ', listaJogadores[jogadorAtual])

    else:
        continuarTurno = str(input('\nVocê deseja continuar? [S/N] ')).strip().upper()[0]
        print("\n")
        if (continuarTurno == "N"):
            pontos[jogadorAtual] += cerebros
            jogadorAtual += 1
            dadosSorteados = []
            tiros = 0
            cerebros = 0
            passos = 0

            if (jogadorAtual == len(listaJogadores)):
                jogadorAtual = 0

    if pontos [jogadorAtual] >= 13:
        print('Parabéns', listaJogadores[jogadorAtual], 'você VENCEU!!!')
        #print("Finalizando o protótipo do jogo")
        break

    dadosSorteados.clear()

    for i in range (0, numJogadores):
        print(listaJogadores[i], pontos[i], 'pontos', end='\n')
    print()

print("Fim de Jogo!")
