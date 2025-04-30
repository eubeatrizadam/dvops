from src.main import *
from unittest.mock import patch

def soma(a, b):
    return a + b

def test_soma():
    assert soma(2, 3) == 5

def test_soma_negativos():
    assert soma(-2, -3) == -5

def multi(a, b):
    return a * b

def test_multi
    assert multi(2, 2) == 4