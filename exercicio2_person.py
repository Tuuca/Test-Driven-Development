import re
from dataclasses import dataclass, field


@dataclass
class Email:
    id: int
    name: str


@dataclass
class Person:
    id: int
    name: str
    age: int
    emails: list[Email] = field(default_factory=list)


class PersonDAO:
    """Regras de validação para inclusão de uma pessoa."""

    @staticmethod
    def save(person: Person) -> None:
        errors = PersonDAO.isValidToInclude(person)
        if errors:
            raise ValueError("; ".join(errors))

    @staticmethod
    def isValidToInclude(person: Person) -> list[str]:
        errors: list[str] = []

        name_parts = person.name.split()
        if len(name_parts) < 2 or not all(part.isalpha() for part in name_parts):
            errors.append("Nome deve ter ao menos duas partes e conter apenas letras.")

        if not isinstance(person.age, int) or isinstance(person.age, bool) or not 1 <= person.age <= 200:
            errors.append("Idade deve estar entre 1 e 200.")

        if not person.emails:
            errors.append("Pessoa deve possuir ao menos um e-mail.")
        elif any(
            not isinstance(email.name, str)
            or re.fullmatch(r"[^@\s]+@[^@.\s]+\.[^@.\s]+", email.name) is None
            for email in person.emails
        ):
            errors.append("E-mail deve estar no formato parte@parte.parte.")

        return errors
