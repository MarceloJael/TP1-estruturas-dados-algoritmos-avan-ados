import heapq

# Exemplo com Heap (min-heap com heapq)
print("=== Exemplo de Heap ===")
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
print("Menor valor:", heapq.heappop(heap))  # Deve mostrar 2

# Exemplo com Trie
print("\n=== Exemplo de Trie ===")

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


trie = Trie()
trie.insert("casa")
trie.insert("carro")
print("Prefixo 'ca' encontrado?", trie.search_prefix("ca"))  # Deve retornar True
print("Prefixo 'mo' encontrado?", trie.search_prefix("mo"))  # Deve retornar False
