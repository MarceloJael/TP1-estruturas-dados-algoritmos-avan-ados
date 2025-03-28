class TrieNode:
    def __init__(self):
        self.filhos = {}
        self.fim_palavra = False

class Trie:
    def __init__(self):
        self.raiz = TrieNode()

    def inserir(self, palavra):
        no = self.raiz
        for letra in palavra:
            if letra not in no.filhos:
                no.filhos[letra] = TrieNode()
            no = no.filhos[letra]
        no.fim_palavra = True

    def buscar(self, palavra):
        no = self.raiz
        for letra in palavra:
            if letra not in no.filhos:
                return False
            no = no.filhos[letra]
        return no.fim_palavra

if __name__ == "__main__":
    trie = Trie()
    palavras = ["casa", "carro", "cadeira", "cachorro"]
    for p in palavras:
        trie.inserir(p)

    testes = ["casa", "carro", "café", "cadeira", "gato"]
    for t in testes:
        print(f"'{t}' encontrado? {trie.buscar(t)}")
