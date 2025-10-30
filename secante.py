from math import cos


def secante(valor):
    if cos(valor) == 0:
        raise ValueError(
            "O ângulo resulta em uma secante indefinida (divisão por zero)."
        )
    return 1 / cos(valor)


if __name__ == "__main__":
    angulo = float(input("Digite o ângulo em radianos: "))
    try:
        resultado = secante(angulo)
        print(f"A secante de {angulo} radianos é: {resultado}")
    except ValueError as e:
        print(e)
