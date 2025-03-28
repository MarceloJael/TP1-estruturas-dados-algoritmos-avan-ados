class MaxHeap:
    def __init__(self):
        self.heap = []

    def inserir(self, valor):
        self.heap.append(valor)
        self._subir(len(self.heap) - 1)

    def _subir(self, i):
        pai = (i - 1) // 2
        if i > 0 and self.heap[i] > self.heap[pai]:
            self.heap[i], self.heap[pai] = self.heap[pai], self.heap[i]
            self._subir(pai)

    def mostrar_heap(self):
        return self.heap

if __name__ == "__main__":
    heap = MaxHeap()
    elementos = [50, 30, 40, 10, 20, 35]
    for el in elementos:
        heap.inserir(el)
    print("Antes:", heap.mostrar_heap())

    heap.inserir(45)
    print("Depois de inserir 45:", heap.mostrar_heap())
