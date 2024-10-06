import heapq
from collections import Counter, defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freqs):
    priority_queue = [Node(char, freq) for char, freq in freqs.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def build_codes(node, prefix='', codebook=defaultdict()):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        build_codes(node.left, prefix + '0', codebook)
        build_codes(node.right, prefix + '1', codebook)
    return codebook

def huffman_encoding(text):
    freqs = Counter(text)
    root = build_huffman_tree(freqs)
    codebook = build_codes(root)
    encoded_text = ''.join(codebook[char] for char in text)
    return encoded_text, codebook

def huffman_decoding(encoded_text, codebook):
    reverse_codebook = {v: k for k, v in codebook.items()}
    decoded_text = ''
    buffer = ''
    for bit in encoded_text:
        buffer += bit
        if buffer in reverse_codebook:
            decoded_text += reverse_codebook[buffer]
            buffer = ''
    return decoded_text

# Test
text = "this is an example for huffman encoding"
encoded_text, codebook = huffman_encoding(text)
decoded_text = huffman_decoding(encoded_text, codebook)
print("Encoded:", encoded_text)
print("Decoded:", decoded_text)
