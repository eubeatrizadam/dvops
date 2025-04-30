import random
from time import sleep

# Variáveis globais para testes e execução
listaJogadores = []
pontos = []

def dadoVerde():
    return ("C", "P", "C", "T", "P", "C")

def dadoAmarelo():
    return ("T", "P", "C", "T", "P", "C")

def dadoVermelho():
    return ("T", "P", "T", "C", "P", "T")

# Executa o jogo apenas se for o script principal
if __name__ == "__main__":
    print("\n ZOMBIE DICE \n")
    print("Seja bem-vindo ao jogo Zombie Dice!\n")

    # Leitura do número de jogadores
    numJogadores = 0
    while numJogadores < 2:
        numJogadores = int(input("Informe a quantidade de jogadores: "))
        print(f"O total de jogadores é {numJogadores}")
        if numJogadores < 2:
            print("AVISO: Você precisa de pelo menos 2 jogadores!")

    # Cadastro dos jogadores
    for c in range(numJogadores):
        nome = input(f'Digite o nome do {c + 1}º jogador: ').upper()
        listaJogadores.append(nome)

    # Lista de dados do jogo
    listaDados = (
        [dadoVerde()] * 6 +
        [dadoAmarelo()] * 4 +
        [dadoVermelho()] * 3
    )

    print("\nIniciando o jogo!\n")

    jogadorAtual = 0
    dadosSorteados = []
    tiros = 0
    cerebros = 0
    passos = 0

    # Inicializa os pontos de todos os jogadores com 0
    pontos = [0] * numJogadores

    def sorteamentoDados():
        global dadosSorteados
        for _ in range(3):
            dado = random.choice(listaDados)
            cor = (
                "VERDE" if dado == dadoVerde() else
                "AMARELO" if dado == dadoAmarelo() else
                "VERMELHO"
            )
            print("O dado sorteado foi", cor)
            dadosSorteados.append(dado)
            sleep(1)

    while True:
        print('Turno do jogador:', listaJogadores[jogadorAtual])

        sorteamentoDados()

        for dado in dadosSorteados:
            face = random.choice(dado)
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
        print("CÉREBROS:", cerebros)
        print("PASSOS -", passos)
        print("TIROS:", tiros)

        if tiros > 2:
            print(f'Você perdeu essa rodada! Levou {tiros} tiros\n')
            tiros = cerebros = passos = 0
            dadosSorteados.clear()
            jogadorAtual = (jogadorAtual + 1) % numJogadores
            print('Indo para a próxima rodada, jogador:', listaJogadores[jogadorAtual])
            continue

        continuar = input('\nVocê deseja continuar? [S/N] ').strip().upper()
        if continuar == "N":
            pontos[jogadorAtual] += cerebros
            jogadorAtual = (jogadorAtual + 1) % numJogadores
            dadosSorteados.clear()
            tiros = cerebros = passos = 0

        if pontos[jogadorAtual] >= 13:
            print('Parabéns', listaJogadores[jogadorAtual], 'você VENCEU!!!')
            break

        dadosSorteados.clear()

        print("\nPLACAR ATUAL:")
        for i in range(numJogadores):
            print(f"{listaJogadores[i]}: {pontos[i]} ponto(s)")
        print()

    print("Fim de Jogo!")
