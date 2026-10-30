# Test Driven Development (TDD) com Python

Implementação dos três exercícios solicitados usando Python e `pytest`.

## Requisitos

- Python 3.9 ou superior
- `pytest` e `pytest-cov`

## Build e execução

Python não exige uma etapa de compilação para este projeto; a preparação
equivalente ao build é a criação do ambiente virtual e a instalação das
dependências.

No Windows, a partir da pasta do projeto:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install pytest pytest-cov
py -m pytest
```

Os módulos de produção são [exercicio1_triangulo.py](./exercicio1_triangulo.py),
[exercicio2_person.py](./exercicio2_person.py) e
[exercicio3_salario.py](./exercicio3_salario.py). As suítes correspondentes são
os arquivos `test_exercicio*.py`.

## Cobertura por exercício

Os comandos abaixo executam cada suíte e geram uma evidência de cobertura
individual em terminal e em HTML:

```powershell
py -m pytest test_exercicio1_triangulo.py --cov=exercicio1_triangulo --cov-report=term-missing --cov-report=html:htmlcov/exercicio1
py -m pytest test_exercicio2_person.py --cov=exercicio2_person --cov-report=term-missing --cov-report=html:htmlcov/exercicio2
py -m pytest test_exercicio3_salario.py --cov=exercicio3_salario --cov-report=term-missing --cov-report=html:htmlcov/exercicio3
```

Cada comando mostra no terminal as linhas cobertas e não cobertas. Os relatórios
HTML ficam em `htmlcov/exercicio1`, `htmlcov/exercicio2` e `htmlcov/exercicio3`
e podem ser abertos no respectivo `index.html`.

### Evidências obtidas

Os comandos acima foram executados individualmente. Os resultados foram:

| Exercício | Suíte | Testes aprovados | Cobertura do código |
|---|---|---:|---:|
| 1 - Triângulo | `test_exercicio1_triangulo.py` | 20 | 100% |
| 2 - Person | `test_exercicio2_person.py` | 15 | 100% |
| 3 - Salário | `test_exercicio3_salario.py` | 9 | 100% |

No total, a execução consolidada aprovou **44 testes** e também apresentou
**100% de cobertura** dos três módulos de produção.

Para executar todos os testes com cobertura consolidada:

```powershell
py -m pytest --cov=. --cov-report=term-missing --cov-report=html
```
