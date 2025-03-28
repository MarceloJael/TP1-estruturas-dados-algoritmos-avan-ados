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

    def exibir(self, no=None, prefixo=""):
        if no is None:
            no = self.raiz
        for letra, filho in no.filhos.items():
            print(prefixo + letra)
            self.exibir(filho, prefixo + letra)

if __name__ == "__main__":
    trie = Trie()
    palavras = ["casa", "carro", "caminhão", "cachorro", "cadeira"]
    for p in palavras:
        trie.inserir(p)

    print("Estrutura hierárquica da Trie:")
    trie.exibir()
