import pytest
from src.desconto import Desconto_normal, Desconto_vip

def test_desconto_normal():
    desconto = Desconto_normal()
    resultado = desconto.calcular(100)
    assert resultado == 10, f"Esperado 10, mas obteve {resultado}"

@pytest.fixture

def desconto_vip():
    return Desconto_vip()

def test_desconto_vip_100(desconto_vip):
    assert desconto_vip.calcular(100) == 20

def test_desconto_vip_200(desconto_vip):
    assert desconto_vip.calcular(200) == 40