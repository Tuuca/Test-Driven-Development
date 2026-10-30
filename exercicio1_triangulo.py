class Triangulo:
    """Classifica três lados de um triângulo."""

    def classificar(self, lado_a: int, lado_b: int, lado_c: int) -> str:
        lados = (lado_a, lado_b, lado_c)

        if any(not isinstance(lado, int) or isinstance(lado, bool) or lado <= 0 for lado in lados):
            return "inválido"

        if (
            lado_a + lado_b <= lado_c
            or lado_a + lado_c <= lado_b
            or lado_b + lado_c <= lado_a
        ):
            return "inválido"

        if lado_a == lado_b == lado_c:
            return "equilátero"
        if lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
            return "isósceles"
        return "escaleno"
