import pytest
import sys

sys.path.append("../")

from calculadora.calculadora import Calculadora


def test_soma():
    assert Calculadora.calcula(expressao='5+5+15') == 25

def test_subtracao():
    assert Calculadora.calcula(expressao='10-15 -5- 7') == -17

def test_multiplicacao():
    assert Calculadora.calcula(expressao='10 * 15') == 150

def test_divisao():
    assert Calculadora.calcula(expressao='10/5') == 2

def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        assert Calculadora.calcula(expressao='5/0')

def test_multiplas_operacoes():
    assert Calculadora.calcula(expressao='(5 * 3 + 5 /5 - 8 ) + 5**2') == 33

def test_expressao_invalida():
    with pytest.raises(Exception):
        assert Calculadora.calcula(expressao='5 + a')