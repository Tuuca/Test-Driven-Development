import pytest

from exercicio3_salario import CalculadoraSalario, Cargo, Funcionario


@pytest.mark.parametrize(
    "cargo,salario,esperado",
    [
        (Cargo.DESENVOLVEDOR, 3000, 2400),
        (Cargo.DESENVOLVEDOR, 2999, 2699.1),
        (Cargo.DBA, 2000, 1500),
        (Cargo.DBA, 1999, 1699.15),
        (Cargo.TESTADOR, 2000, 1500),
        (Cargo.TESTADOR, 1999, 1699.15),
        (Cargo.GERENTE, 5000, 3500),
        (Cargo.GERENTE, 4999, 3999.2),
    ],
)
def test_calcula_salario_liquido_por_cargo_e_limite(cargo, salario, esperado):
    funcionario = Funcionario("Ana Silva", "ana@example.com", salario, cargo)
    assert CalculadoraSalario.calcular_salario_liquido(funcionario) == pytest.approx(esperado)


def test_rejeita_cargo_invalido():
    funcionario = Funcionario("Ana Silva", "ana@example.com", 3000, "ARQUITETO")
    with pytest.raises(ValueError):
        CalculadoraSalario.calcular_salario_liquido(funcionario)
