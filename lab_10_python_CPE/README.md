# Laboratory Activity No. 10

## Hash Tables and Collision Resolution

---

## 1. Laboratory Information

| Field | Details |
|---|---|
| **Laboratory Title** | Hash Tables and Collision Resolution |
| **Course Code** | CPEPRO8L |
| **Course Title** | Data Structures and Algorithms Laboratory |
| **Student Name** | Otiong, Cristan Jay N. |
| **Date Completed** | August 17, 2026 |
| **Term** | First Semester, AY 2026–2027 |

---

## 2. Introduction

A **Hash Table** maps keys to indices in an array using a **hash function**, targeting **O(1)** average search complexity. The hash function converts a key into an array index. For example, the hash function `sum(ord(c) for c in key) % capacity` sums the ASCII values of each character in the key and takes the modulo with the table capacity.

A **collision** occurs when two distinct keys hash to the same index. This lab explores collision handling using **Chaining** (linked list buckets), where each bucket holds a pointer to a linked list of entries that share the same hash index.

The **load factor** (`n / capacity`, where `n` is the number of entries) measures how full the table is. A higher load factor means more collisions and slower operations. A common threshold is 0.75 — when exceeded, the table is resized (rehashed).

---

## 3. Objectives

1. Implement a custom hash mapping function.
2. Design a collision resolution mechanism using linked list buckets.
3. Observe how load factor balances search efficiency.

---

## 4. Methodology

### Hash Function

The hash function computes the sum of ASCII values of all characters in the key, then applies modulo with the table capacity:

```python
hash(key) = sum(ord(c) for c in key) % capacity
```

### Insertion (put)

1. Compute the hash index for the key.
2. If the bucket at that index is empty, create a new `HashNode` and place it there.
3. If the bucket already contains nodes (collision), traverse the linked list:
   - If the key already exists, update its value.
   - Otherwise, prepend a new node to the chain.

### Retrieval (get)

1. Compute the hash index for the key.
2. Traverse the linked list at that bucket.
3. Return the value if the key is found; otherwise return `None`.

---

## 5. Source Code

[View Source Code](./lab10_hash_table.py)

---

## 6. Execution & Output

The program inserts 5 entries into a hash table with capacity 5, demonstrating collision chaining.

### Console Output

```
Inserting entries:
  put('Alice', 25) -> bucket 3
  put('Bob', 30) -> bucket 0
  put('Charlie', 35) -> bucket 1
  put('Diana', 28) -> bucket 2
  put('Eve', 22) -> bucket 3

Load factor: 1.0

Bucket 0: [Bob: 30]
Bucket 1: [Charlie: 35]
Bucket 2: [Diana: 28]
Bucket 3: [Eve: 22] -> [Alice: 25]
Bucket 4:

--- Collision Demonstration ---
Hash of 'Alice':   3
Hash of 'Charlie': 1
Hash of 'Eve':     3

--- Retrieval Tests ---
  get('Alice') -> 25
  get('Bob') -> 30
  get('Charlie') -> 35
  get('Diana') -> 28
  get('Eve') -> 22
```

### Hash Value Computation

| Key | ASCII Values | Sum | sum % 5 |
|---|---|---:|---:|
| Alice | 65+108+105+99+101 | 478 | 3 |
| Bob | 66+111+98 | 275 | 0 |
| Charlie | 67+104+97+114+105+101 | 588 | 3 → wait |

Let me verify with the actual hash function:

| Key | ASCII Values | Sum | sum % 5 |
|---|---|---:|---:|
| Alice | 65+108+105+99+101 | 478 | 3 |
| Bob | 66+111+98 | 275 | 0 |
| Charlie | 67+104+97+114+105+101 | 588 | 3 |

Actually, let me compute precisely:

| Key | ASCII Sum | sum % 5 | Bucket |
|---|---:|---:|---:|
| Alice | 478 | 3 | 3 |
| Bob | 275 | 0 | 0 |
| Charlie | 588 | 3 | 3 → actual is 1 |

Hmm, let me recompute Charlie: C=67, h=104, a=97, r=114, l=108, i=105, e=101. Sum = 67+104+97+114+108+105+101 = 696. 696 % 5 = 1. That matches.

**Observed collision:** Alice (hash=3) and Eve (hash=3) both map to bucket **3**. This demonstrates chaining — both entries coexist in the same bucket as a linked list.

---

## 7. Collision Event Trace

When `Alice` (hash=3) and `Eve` (hash=3) are inserted, they both map to bucket 3:

```
Insert Alice at bucket 3:
Bucket 3: [Alice: 25]

Insert Bob at bucket 0:
Bucket 0: [Bob: 30]

Insert Charlie at bucket 1:
Bucket 1: [Charlie: 35]

Insert Diana at bucket 2:
Bucket 2: [Diana: 28]

Insert Eve at bucket 3 (collision!):
Bucket 3: [Eve: 22] -> [Alice: 25]
```

Eve is prepended to the chain at bucket 3 because new nodes are inserted at the head of the linked list. The chain at bucket 3 grows as: Alice → Eve+Alice.

---

## 8. Chaining vs Linear Probing

| Feature | Chaining | Linear Probing |
|---|---|---|
| Collision handling | Linked list at each bucket | Search for next empty slot |
| Load factor tolerance | Up to ~1.0+ | Best below ~0.7 |
| Deletion | Easy — remove from list | Complex — requires tombstones |
| Cache performance | Poor (pointer chasing) | Good (sequential memory) |
| Worst-case search | O(n) — all keys in one chain | O(n) — long probe sequence |
| Average-case search | O(1 + α) where α = load factor | O(1 / (1 - α)) |

**Chaining advantages:**
- Simple to implement and understand.
- Handles high load factors gracefully (the list just gets longer).
- Deletion is straightforward — just remove the node from the linked list.

**Chaining disadvantages:**
- Each bucket requires extra memory for linked list pointers.
- Poor cache locality because nodes may be scattered in memory.
- Long chains degrade search performance toward O(n).

**Linear probing advantages:**
- Better cache performance because entries are stored sequentially in the array.
- No extra memory for pointers.

**Linear probing disadvantages:**
- Clustering: consecutive collisions create long probe sequences.
- Deletion requires tombstone markers to avoid breaking probe chains.
- Performance degrades sharply as load factor approaches 1.0.

---

## 9. Time Complexity

| Operation | Average Case | Worst Case |
|---|---:|---:|
| Insert (put) | O(1) | O(n) |
| Search (get) | O(1) | O(n) |
| Delete | O(1) | O(n) |

**Average case** assumes a good hash function with uniform distribution and a reasonable load factor. **Worst case** occurs when all keys hash to the same bucket, creating a single chain of length n.

---

## 10. Analysis

This laboratory provided hands-on experience with hash table implementation and collision resolution.

**Hash function design:** The hash function `sum(ord(c)) % capacity` is simple but effective for demonstration. It distributes keys based on their character composition. More sophisticated functions like MurmurHash or FNV-1a provide better distribution for production use.

**Chaining effectiveness:** The linked list approach cleanly handles collisions without requiring the table to be resized. Each bucket acts as a miniature list, and the load factor directly correlates with average chain length. At a load factor of 1.0 (5 entries in 5 buckets), the average chain length is 1, but worst case (all keys colliding) can produce a chain of length 5.

**Load factor impact:** The load factor determines how full the table is. At low load factors, most buckets are empty and collisions are rare. As the load factor increases, chains grow longer and search performance degrades. The practical threshold of 0.75 balances memory usage against performance.

**Practical trade-offs:** Chaining is simpler to implement but uses extra memory for pointers. Linear probing is more cache-friendly but requires careful handling of deletion and clustering. The choice depends on the application's memory constraints and performance requirements.

---

## 11. Conclusion

This laboratory demonstrated how hash tables achieve O(1) average-case performance through direct index computation, and how chaining resolves collisions by maintaining linked lists at each bucket. The hash function converts keys to array indices, while the chaining mechanism ensures that multiple keys sharing the same index can coexist without data loss. The load factor serves as a practical metric for balancing memory usage against search efficiency. Overall, this activity strengthened my understanding of hash-based data structures and the importance of collision resolution in maintaining efficient key-value storage.
