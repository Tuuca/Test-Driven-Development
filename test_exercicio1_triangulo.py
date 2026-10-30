import pytest

from exercicio1_triangulo import Triangulo


@pytest.fixture
def triangulo():
    return Triangulo()


def test_classifica_triangulo_escaleno_valido(triangulo):
    assert triangulo.classificar(3, 4, 5) == "escaleno"


@pytest.mark.parametrize("lados", [(3, 3, 4), (3, 4, 3), (4, 3, 3)])
def test_classifica_todas_as_permutacoes_de_isosceles(triangulo, lados):
    assert triangulo.classificar(*lados) == "isósceles"


def test_classifica_triangulo_equilatero_valido(triangulo):
    assert triangulo.classificar(5, 5, 5) == "equilátero"


@pytest.mark.parametrize("lados", [(0, 3, 4), (-1, 3, 4), (0, 0, 0)])
def test_rejeita_lados_zero_ou_negativos(triangulo, lados):
    assert triangulo.classificar(*lados) == "inválido"


@pytest.mark.parametrize("lados", [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)])
def test_rejeita_soma_de_dois_lados_igual_ao_terceiro(triangulo, lados):
    assert triangulo.classificar(*lados) == "inválido"


@pytest.mark.parametrize("lados", [(1, 2, 4), (1, 4, 2), (2, 1, 4), (2, 4, 1), (4, 1, 2), (4, 2, 1)])
def test_rejeita_soma_de_dois_lados_menor_que_o_terceiro(triangulo, lados):
    assert triangulo.classificar(*lados) == "inválido"
