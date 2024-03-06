import pytest
from exercicio1 import Calcular_desconto

def test_calculo_desconto_0():
    valor_sem_desconto, valor_com_desconto = Calcular_desconto(20, 5)
    assert valor_sem_desconto == 100
    assert valor_com_desconto == 100

def test_calculo_desconto_5():
    valor_sem_desconto, valor_com_desconto = Calcular_desconto(20, 10)
    assert valor_sem_desconto == 200
    assert valor_com_desconto == 190

def test_calculo_desconto_10():
    valor_sem_desconto, valor_com_desconto = Calcular_desconto(20, 100)
    assert valor_sem_desconto == 2000
    assert valor_com_desconto == 1800

def test_calculo_desconto_15():
    valor_sem_desconto, valor_com_desconto = Calcular_desconto(20, 1000)
    assert valor_sem_desconto == 20000
    assert valor_com_desconto == 17000