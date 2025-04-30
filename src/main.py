import random
from time import sleep

def dadoVerde():
    return ("C", "P", "C", "T", "P", "C")

def dadoAmarelo():
    return ("T", "P", "C", "T", "P", "C")

def dadoVermelho():
    return ("T", "P", "T", "C", "P", "T")

def sorteamentoDados(listaDados):
    dadosSorteados = []
    for _ in range(3):
        numSorteado = random.randrange(13)
        dadoSorteado = listaDados[numSorteado]
        if dadoSorteado == dadoVerde():
            corDado = "VERDE"
        elif dadoSorteado == dadoAmarelo():
            corDado = "AMARELO"
        elif dadoSorteado == dadoVermelho():
            corDado = "VERMELHO"
        dadosSorteados.append((dadoSorteado, corDado))
    return dadosSorteados

def iniciar_jogo():
    print("\nZOMBIE DICE\n")
    print("Seja bem-vindo ao jogo Zombie Dice!\n")

    numJogadores = 0
    while numJogadores < 2:
        numJogadores = int(input("Informe a quantidade de jogadores: "))
        print(f"O total de jogadores é {numJogadores}")
        if numJogadores < 2:
            print("AVISO: Você precisa de pelo menos 2 jogadores!")

    listaJogadores = []
    pontos = [0] * numJogadores

    for c in range(numJogadores):
        nome = input(f'Digite o nome do {c + 1}º jogador: ').upper()
        listaJogadores.append(nome)

    listaDados = [
        dadoVerde(), dadoVerde(), dadoVerde(), dadoVerde(), dadoVerde(), dadoVerde(),
        dadoAmarelo(), dadoAmarelo(), dadoAmarelo(), dadoAmarelo(),
        dadoVermelho(), dadoVermelho(), dadoVermelho()
    ]

    jogadorAtual = 0
    while True:
        print(f'\nTurno do jogador: {listaJogadores[jogadorAtual]}')
        dadosSorteados = sorteamentoDados(listaDados)

        cerebros = 0
        tiros = 0
        passos = 0

        for dadoSorteado, corDado in dadosSorteados:
            numFaces = random.randint(0, 5)
            face = dadoSorteado[numFaces]
            print(f'O dado sorteado foi {corDado} com face: {face}')
            if face == "C":
                print('Você comeu um CÉREBRO!')
                cerebros += 1
            elif face == "T":
                print('Você levou um TIRO!')
                tiros += 1
            else:
                print('Você tirou um PASSO! Sua vítima escapou!')
                passos += 1
            sleep(1)

        print("\n===SCORE ATUAL===")
        print(f"CÉREBROS: {cerebros}")
        print(f"PASSOS: {passos}")
        print(f"TIROS: {tiros}")

        if tiros > 2:
            print(f'Você perdeu essa rodada! Levou {tiros} tiros\n')
            pontos[jogadorAtual] += cerebros
            jogadorAtual = (jogadorAtual + 1) % numJogadores
        else:
            continuarTurno = input('\nVocê deseja continuar? [S/N] ').strip().upper()
            if continuarTurno == "N":
                pontos[jogadorAtual] += cerebros
                jogadorAtual = (jogadorAtual + 1) % numJogadores

        print("\n=== PONTUAÇÃO ATUAL ===")
        for i in range(numJogadores):
            print(f"{listaJogadores[i]}: {pontos[i]} pontos")

        if pontos[jogadorAtual] >= 13:
            print(f'Parabéns {listaJogadores[jogadorAtual]}, você VENCEU!!!')
            break

    print("\nFim de Jogo!")

if __name__ == "__main__":
    iniciar_jogo()
