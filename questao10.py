class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, palavra):
        node = self.root
        for letra in palavra:
            if letra not in node.children:
                node.children[letra] = TrieNode()
            node = node.children[letra]
        node.is_end_of_word = True

    def _buscar_prefixo(self, prefixo):
        node = self.root
        for letra in prefixo:
            if letra not in node.children:
                return None
            node = node.children[letra]
        return node

    def _coletar_palavras(self, node, prefixo, resultados):
        if node.is_end_of_word:
            resultados.append(prefixo)
        for letra, filho in node.children.items():
            self._coletar_palavras(filho, prefixo + letra, resultados)

    def autocomplete(self, prefixo):
        resultados = []
        node = self._buscar_prefixo(prefixo)
        if node:
            self._coletar_palavras(node, prefixo, resultados)
        return resultados

if __name__ == "__main__":
    trie = Trie()
    palavras = ["casa", "carro", "cadeira", "cachorro", "caminhão", "cacto", "cartão"]
    for p in palavras:
        trie.insert(p)

    prefixo = "ca"
    sugestoes = trie.autocomplete(prefixo)
    print(f"Autocomplete para '{prefixo}':", sugestoes)
