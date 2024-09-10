def search(text, word):
    index = text.find(word)
    if index != -1:
        return f"'{word}' found at index {index}."
    return f"'{word}' not found."

# Test
text = "This is a simple text editor."
word = "simple"
print(search(text, word))  # Output: 'simple' found at index 10.
