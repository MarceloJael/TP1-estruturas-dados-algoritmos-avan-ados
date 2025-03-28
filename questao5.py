def indice_pai(i):
    return (i - 1) // 2

def filho_esquerdo(i):
    return 2 * i + 1

def filho_direito(i):
    return 2 * i + 2

if __name__ == "__main__":
    i = 3  # exemplo de índice
    print(f"Índice do pai de {i}: {indice_pai(i)}")
    print(f"Índice do filho esquerdo de {i}: {filho_esquerdo(i)}")
    print(f"Índice do filho direito de {i}: {filho_direito(i)}")
