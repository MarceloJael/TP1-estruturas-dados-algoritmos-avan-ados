class MinHeap:
    def __init__(self):
        self.heap = []

    def inserir(self, valor):
        self.heap.append(valor)
        self._subir(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._descer(0)
        return raiz

    def _subir(self, i):
        pai = (i - 1) // 2
        if i > 0 and self.heap[i] < self.heap[pai]:
            self.heap[i], self.heap[pai] = self.heap[pai], self.heap[i]
            self._subir(pai)

    def _descer(self, i):
        menor = i
        esq = 2 * i + 1
        dir = 2 * i + 2
        if esq < len(self.heap) and self.heap[esq] < self.heap[menor]:
            menor = esq
        if dir < len(self.heap) and self.heap[dir] < self.heap[menor]:
            menor = dir
        if menor != i:
            self.heap[i], self.heap[menor] = self.heap[menor], self.heap[i]
            self._descer(menor)

    def mostrar(self):
        return self.heap

if __name__ == "__main__":
    h = MinHeap()
    for num in [10, 4, 15, 1, 7]:
        h.inserir(num)
    print("Heap inicial:", h.mostrar())
    removido = h.pop()
    print("Removido:", removido)
    print("Heap após remoção:", h.mostrar())
