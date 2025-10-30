#Raiz/ Potencia 
import math

def raiz(numero):
    """Retorna a raiz quadrada de um número."""
    if numero < 0:
        return "Não existe raiz real para números negativos."
    return math.sqrt(numero)

# Exemplo de uso:
print(raiz(9))   # Saída: 3.0
print(raiz(25))  # Saída: 5.0
print(raiz(-4))  # Saída: Não existe raiz real para números negativos.
