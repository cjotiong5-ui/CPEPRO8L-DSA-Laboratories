class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.buckets = [None] * capacity
        self.size = 0

    def _hash(self, key):
        return sum(ord(c) for c in str(key)) % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        current = self.buckets[index]

        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next

        new_node = HashNode(key, value)
        new_node.next = self.buckets[index]
        self.buckets[index] = new_node
        self.size += 1

    def get(self, key):
        index = self._hash(key)
        current = self.buckets[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def load_factor(self):
        return self.size / self.capacity

    def display(self):
        for idx in range(self.capacity):
            chain = []
            temp = self.buckets[idx]
            while temp:
                chain.append(f"[{temp.key}: {temp.value}]")
                temp = temp.next
            print(f"Bucket {idx}: " + " -> ".join(chain))


if __name__ == "__main__":
    ht = HashTable(5)

    print("Inserting entries:")
    entries = [("Alice", 25), ("Bob", 30), ("Charlie", 35), ("Diana", 28), ("Eve", 22)]
    for key, value in entries:
        ht.put(key, value)
        print(f"  put('{key}', {value}) -> bucket {ht._hash(key)}")

    print(f"\nLoad factor: {ht.load_factor()}")
    print()
    ht.display()

    print("\n--- Collision Demonstration ---")
    print(f"Hash of 'Alice':   {ht._hash('Alice')}")
    print(f"Hash of 'Charlie': {ht._hash('Charlie')}")
    print(f"Hash of 'Eve':     {ht._hash('Eve')}")

    print("\n--- Retrieval Tests ---")
    for key, _ in entries:
        result = ht.get(key)
        print(f"  get('{key}') -> {result}")
