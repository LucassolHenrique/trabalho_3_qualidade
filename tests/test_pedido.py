import pytest
from src.pedido import calcular_total_pedido

def test_calcular_total_simples():
    # Caso 1: Teste com itens sem frete e sem cupom
    itens = [{'preco': 20.0, 'quantidade': 2}]
    assert calcular_total_pedido(itens) == 40.0

def test_calcular_total_com_frete():
    # Caso 2: Teste com frete
    itens = [{'preco': 15.0, 'quantidade': 1}]
    frete = 5.0
    assert calcular_total_pedido(itens, frete=frete) == 20.0

def test_calcular_total_com_cupom_fixo():
    # Caso 3: Teste com cupom de desconto fixo
    itens = [{'preco': 50.0, 'quantidade': 1}]
    cupom = {'tipo': 'fixo', 'valor': 10.0}
    assert calcular_total_pedido(itens, cupom=cupom) == 40.0

def test_calcular_total_com_cupom_percentual():
    # Caso 4: Teste com cupom de desconto percentual
    itens = [{'preco': 100.0, 'quantidade': 1}]
    cupom = {'tipo': 'percentual', 'valor': 10.0}
    assert calcular_total_pedido(itens, cupom=cupom) == 90.0

def test_calcular_total_nao_negativo():
    # Caso 5: Garantir que o valor total nunca seja negativo
    itens = [{'preco': 5.0, 'quantidade': 1}]
    cupom = {'tipo': 'fixo', 'valor': 50.0}
    assert calcular_total_pedido(itens, cupom=cupom) == 0.0
