import unittest
from collections import Counter

def dadoVerde():
    return ("C", "P", "C", "T", "P", "C")

def dadoAmarelo():
    return ("T", "P", "C", "T", "P", "C")

def dadoVermelho():
    return ("T", "P", "T", "C", "P", "T")

class TestZombieDice(unittest.TestCase):

    def test_dado_verde(self):
        dado = dadoVerde()
        self.assertEqual(len(dado), 6)
        contagem = Counter(dado)
        self.assertEqual(contagem['C'], 3)
        self.assertEqual(contagem['P'], 2)
        self.assertEqual(contagem['T'], 1)

    def test_dado_amarelo(self):
        dado = dadoAmarelo()
        self.assertEqual(len(dado), 6)
        contagem = Counter(dado)
        self.assertEqual(contagem['C'], 2)
        self.assertEqual(contagem['P'], 2)
        self.assertEqual(contagem['T'], 2)

    def test_dado_vermelho(self):
        dado = dadoVermelho()
        self.assertEqual(len(dado), 6)
        contagem = Counter(dado)
        self.assertEqual(contagem['C'], 1)
        self.assertEqual(contagem['P'], 2)
        self.assertEqual(contagem['T'], 3)

    def test_jogadores_inicialmente_vazios(self):
    self.assertEqual(listaJogadores, [])

    def test_pontuacao_inicial(self):
        # Supondo 0 jogadores inicialmente
        self.assertTrue(all(p == 0 for p in pontos))

if __name__ == '__main__':
    unittest.main()