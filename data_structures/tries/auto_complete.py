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

    def auto_complete(self, prefix):
        def dfs(node, prefix):
            if node.is_end_of_word:
                result.append(prefix)

            for char in node.children:
                dfs(node.children[char], prefix + char)

        result = []
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        dfs(node, prefix)
        return result

# Test
trie = Trie()
trie.insert("cat")
trie.insert("car")
trie.insert("cart")
trie.insert("dog")
print(trie.auto_complete("ca"))  # Output: ['cat', 'car', 'cart']
