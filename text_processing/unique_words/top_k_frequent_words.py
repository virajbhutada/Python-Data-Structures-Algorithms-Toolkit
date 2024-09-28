from collections import Counter

def top_k_frequent(words, k):
    count = Counter(words)
    return [word for word, _ in count.most_common(k)]

# Test
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(top_k_frequent(words, k))  # Output: ['i', 'love']
