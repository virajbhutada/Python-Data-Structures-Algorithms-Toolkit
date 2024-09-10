class OpenAddressingHashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def probe(self, index):
        i = 0
        while self.table[(index + i) % self.size] is not None:
            if self.table[(index + i) % self.size][0] == key:
                return (index + i) % self.size
            i += 1
        return (index + i) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        index = self.probe(index)
        self.table[index] = (key, value)

    def get(self, key):
        index = self.hash_function(key)
        index = self.probe(index)
        if self.table[index] is not None and self.table[index][0] == key:
            return self.table[index][1]
        return None

    def remove(self, key):
        index = self.hash_function(key)
        index = self.probe(index)
        if self.table[index] is not None and self.table[index][0] == key:
            self.table[index] = None

# Test
hash_table = OpenAddressingHashTable()
hash_table.insert("name", "Charlie")
print(hash_table.get("name"))  # Output: Charlie
hash_table.remove("name")
print(hash_table.get("name"))  # Output: None
