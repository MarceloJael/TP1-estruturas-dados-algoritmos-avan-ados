class Tarefa:
    def __init__(self, nome, prioridade):
        self.nome = nome
        self.prioridade = prioridade

    def __lt__(self, outra):
        return self.prioridade < outra.prioridade

    def __repr__(self):
        return f"{self.nome} (Prioridade {self.prioridade})"

class FilaDePrioridade:
    def __init__(self):
        self.heap = []

    def adicionar_tarefa(self, tarefa):
        self.heap.append(tarefa)
        self._subir(len(self.heap) - 1)

    def executar_tarefa(self):
        if not self.heap:
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

    def mostrar_fila(self):
        return self.heap

if __name__ == "__main__":
    fila = FilaDePrioridade()
    fila.adicionar_tarefa(Tarefa("Backup do sistema", 2))
    fila.adicionar_tarefa(Tarefa("Atualizar antivírus", 1))
    fila.adicionar_tarefa(Tarefa("Gerar relatório", 3))

    print("Fila de tarefas:", fila.mostrar_fila())

    print("\nExecutando tarefas por prioridade:")
    while fila.mostrar_fila():
        print("Executando:", fila.executar_tarefa())
