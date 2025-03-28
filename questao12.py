class TrieNode:
    def __init__(self):
        self.children = {}
        self.fim_palavra = False

class Trie:
    def __init__(self):
        self.raiz = TrieNode()

    def inserir(self, palavra):
        no = self.raiz
        for letra in palavra:
            if letra not in no.children:
                no.children[letra] = TrieNode()
            no = no.children[letra]
        no.fim_palavra = True

    def _buscar_prefixo(self, prefixo):
        no = self.raiz
        for letra in prefixo:
            if letra not in no.children:
                return None
            no = no.children[letra]
        return no

    def _coletar(self, no, prefixo, resultado):
        if no.fim_palavra:
            resultado.append(prefixo)
        for letra, filho in no.children.items():
            self._coletar(filho, prefixo + letra, resultado)

    def autocomplete(self, prefixo):
        resultado = []
        no = self._buscar_prefixo(prefixo)
        if no:
            self._coletar(no, prefixo, resultado)
        return resultado

# Teste
if __name__ == "__main__":
    trie = Trie()
    palavras = ["casa", "carro", "cachorro", "cadeira", "cartão"]
    for p in palavras:
        trie.inserir(p)

    prefixo = "ca"
    sugestoes = trie.autocomplete(prefixo)
    print(f"Palavras com prefixo '{prefixo}': {sugestoes}")
