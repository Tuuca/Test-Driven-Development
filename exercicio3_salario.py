from dataclasses import dataclass
from enum import Enum


class Cargo(str, Enum):
    DESENVOLVEDOR = "DESENVOLVEDOR"
    DBA = "DBA"
    TESTADOR = "TESTADOR"
    GERENTE = "GERENTE"


@dataclass
class Funcionario:
    nome: str
    email: str
    salario_base: float
    cargo: Cargo


class CalculadoraSalario:
    @staticmethod
    def calcular_salario_liquido(funcionario: Funcionario) -> float:
        descontos = {
            Cargo.DESENVOLVEDOR: (0.20, 0.10, 3000),
            Cargo.DBA: (0.25, 0.15, 2000),
            Cargo.TESTADOR: (0.25, 0.15, 2000),
            Cargo.GERENTE: (0.30, 0.20, 5000),
        }
        try:
            desconto_alto, desconto_baixo, limite = descontos[funcionario.cargo]
        except KeyError as error:
            raise ValueError("Cargo inválido.") from error

        desconto = desconto_alto if funcionario.salario_base >= limite else desconto_baixo
        return funcionario.salario_base * (1 - desconto)
