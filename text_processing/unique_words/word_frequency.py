from collections import Counter

def word_frequency(text):
    words = text.split()
    return dict(Counter(words))

# Test
text = "hello world hello"
print(word_frequency(text))  # Output: {'hello': 2, 'world': 1}
