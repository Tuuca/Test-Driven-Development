import pytest

from exercicio2_person import Email, Person, PersonDAO


def pessoa_valida():
    return Person(1, "Maria Silva", 30, [Email(1, "maria@example.com")])


def test_person_valida_pode_ser_incluida():
    assert PersonDAO.isValidToInclude(pessoa_valida()) == []


@pytest.mark.parametrize("name", ["Maria", "Maria123 Silva", "Maria Silva-"])
def test_rejeita_nome_invalido(name):
    errors = PersonDAO.isValidToInclude(Person(1, name, 30, [Email(1, "maria@example.com")]))
    assert any("Nome" in error for error in errors)


@pytest.mark.parametrize("age", [0, 201, -1])
def test_rejeita_idade_fora_do_intervalo(age):
    errors = PersonDAO.isValidToInclude(Person(1, "Maria Silva", age, [Email(1, "maria@example.com")]))
    assert any("Idade" in error for error in errors)


def test_rejeita_pessoa_sem_email():
    errors = PersonDAO.isValidToInclude(Person(1, "Maria Silva", 30))
    assert any("e-mail" in error for error in errors)


@pytest.mark.parametrize("email", ["mariaexample.com", "maria@", "@example.com", "maria@example", "maria@.com"])
def test_rejeita_email_fora_do_formato(email):
    errors = PersonDAO.isValidToInclude(Person(1, "Maria Silva", 30, [Email(1, email)]))
    assert any("E-mail" in error for error in errors)


def test_save_lanca_erro_para_person_invalida():
    with pytest.raises(ValueError):
        PersonDAO.save(Person(1, "Maria", 30))


def test_save_nao_lanca_erro_para_person_valida():
    PersonDAO.save(pessoa_valida())
