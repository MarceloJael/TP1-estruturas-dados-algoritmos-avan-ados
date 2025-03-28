class MinHeap:
    def __init__(self):
        self.heap = []

    def inserir(self, valor):
        self.heap.append(valor)
        self._subir(len(self.heap) - 1)

    def remover_minimo(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        minimo = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._descer(0)
        return minimo

    def _subir(self, index):
        pai = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[pai]:
            self.heap[index], self.heap[pai] = self.heap[pai], self.heap[index]
            self._subir(pai)

    def _descer(self, index):
        menor = index
        esquerda = 2 * index + 1
        direita = 2 * index + 2

        if esquerda < len(self.heap) and self.heap[esquerda] < self.heap[menor]:
            menor = esquerda
        if direita < len(self.heap) and self.heap[direita] < self.heap[menor]:
            menor = direita

        if menor != index:
            self.heap[index], self.heap[menor] = self.heap[menor], self.heap[index]
            self._descer(menor)

    def mostrar_heap(self):
        return self.heap

if __name__ == "__main__":
    heap = MinHeap()

    # Inserindo elementos
    elementos = [10, 4, 9, 1, 7, 5]
    for el in elementos:
        heap.inserir(el)
        print(f"Inserido {el}: {heap.mostrar_heap()}")

    # Removendo elementos
    print("\nRemovendo elementos:")
    while heap.mostrar_heap():
        minimo = heap.remover_minimo()
        print(f"Removido {minimo}: {heap.mostrar_heap()}")
