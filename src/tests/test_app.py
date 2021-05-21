import sys

sys.path.append("../")
from app import CalculadoraView

calc = CalculadoraView()

def test_get_font():
    assert calc.get_font() == ("Verdana", 18, "bold")

def test_clear_label():
    calc.var = "152"
    calc.equacao.set(calc.var)
    calc.clear_label()
    assert calc.label["text"] == "0"

def test_back_space():
    calc.var = "25"
    calc.equacao.set(calc.var)
    calc.back_space()
    assert calc.label["text"] == "2"

def test_add_valor():
    calc.var = ""
    calc.equacao.set(calc.var)
    calc.add_valor("74")
    assert calc.label["text"] == "74"

def test_calcula_resultado():
    calc.equacao.set("25 + 7")
    calc.calcula_resultado()
    assert calc.label["text"] == "32"