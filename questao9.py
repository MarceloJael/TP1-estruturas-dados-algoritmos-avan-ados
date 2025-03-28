class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

if __name__ == "__main__":
    trie = Trie()
    palavras = ["casa", "carro", "cadeira"]
    for p in palavras:
        trie.insert(p)

    testes = ["casa", "carro", "cachorro", "cadeira", "caminhão"]
    for t in testes:
        print(f"'{t}' encontrado? {trie.search(t)}")
