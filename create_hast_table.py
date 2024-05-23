class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] ==key:
                return pair[1]
            
    def remove(self, key):
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return
hash_table = HashTable()


hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
hash_table.insert("grape", 40)
hash_table.insert("watermelon", 50)

print("Value for apple:", hash_table.get("apple"))
print("Value for banana:", hash_table.get("banana"))
hash_table.insert("banana", 25)
print("Updated Value for 'banana':", hash_table.get("banana"))

hash_table.remove("grape")
print("Value for 'grape':",hash_table.get("grape"))


