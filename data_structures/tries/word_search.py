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

    def word_search(self, board, words):
        result = set()

        def dfs(x, y, node, path):
            if node.is_end_of_word:
                result.add(path)

            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] not in node.children:
                return

            char = board[x][y]
            board[x][y] = "#"
            dfs(x + 1, y, node.children[char], path + char)
            dfs(x - 1, y, node.children[char], path + char)
            dfs(x, y + 1, node.children[char], path + char)
            dfs(x, y - 1, node.children[char], path + char)
            board[x][y] = char

        for word in words:
            self.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, self.root, "")

        return list(result)

# Test
trie = Trie()
board = [
    ['o', 'a', 'n', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
]
words = ["oath", "pea", "eat", "rain"]
print(trie.word_search(board, words))  # Output: ['oath', 'eat']
