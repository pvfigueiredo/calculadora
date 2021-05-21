import pytest
from calculadora import Calculadora


calc = Calculadora()

def test_soma():
    assert calc.calcula('5+5+15') == 25

def test_subtracao():
    assert calc.calcula('10-15 -5- 7') == -17

def test_multiplicacao():
    assert calc.calcula('10 * 15') == 150

def test_divisao():
    assert calc.calcula('10/5') == 2

def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        assert calc.calcula('5/0')

def test_multiplas_operacoes():
    assert calc.calcula('(5 * 3 + 5 /5 - 8 ) + 5**2') == 33

def test_expressao_invalida():
    with pytest.raises(Exception):
        assert calc.calcula('5 + a')