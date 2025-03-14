valores = list(map(int, input("Digite a lista de valores separados por espaço: ").split()))

def is_prime(num):
    """Função para verificar se um número é primo."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def processa_lista(valores):
    """Função que processa a lista e retorna a tupla com os resultados pedidos."""
    
    if len(valores) < 2:
        segundo_maior = None
    else:
        segundo_maior = sorted(set(valores))[-2]
    
    soma_primos = sum(val for val in valores if is_prime(val))
    
    pares = [val for val in valores if val % 2 == 0]
    media_pares = round(sum(pares) / len(pares), 2) if pares else 0.00
    
    return (segundo_maior, soma_primos, media_pares)

resultado = processa_lista(valores)
print(resultado)