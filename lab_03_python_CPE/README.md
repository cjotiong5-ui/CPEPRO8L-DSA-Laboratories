# Laboratory Activity No. 3 — Singly Linked List CRUD Operations

## 1. Laboratory Information

| Field                | Details                                   |
| -------------------- | ----------------------------------------- |
| **Laboratory Title** | Singly Linked List CRUD Operations        |
| **Course Code**      | CPEPRO8L                                  |
| **Course Title**     | Data Structures and Algorithms Laboratory |
| **Student Name**     | Otiong, Cristan Jay N.                    |
| **Date Completed**   | (07/16/26)                           |
| **Term**             | First Semester, AY 2026–2027              |

---

## 2. Introduction

A **Singly Linked List** is a dynamic data structure where elements are stored in non-contiguous memory locations. Each node contains:

* Data
* A pointer (reference) to the next node

Unlike arrays, linked lists allow efficient insertion and deletion without shifting elements.

---

## 3. Objectives

* Create `Node` and `SinglyLinkedList` classes
* Implement CRUD operations:

  * Insert (Head & Tail)
  * Search
  * Delete
* Understand pointer manipulation

---

## 4. Implementation

### Node Class

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

---

### Insert at Head

```python
def insert_head(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
```

---

### Insert at Tail

```python
def insert_tail(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        return

    current = self.head
    while current.next:
        current = current.next

    current.next = new_node
```

---

### Delete Value

```python
def delete_value(self, target):
    if not self.head:
        return False

    if self.head.data == target:
        self.head = self.head.next
        return True

    current = self.head
    while current.next:
        if current.next.data == target:
            current.next = current.next.next
            return True
        current = current.next

    return False
```

---

### Search

```python
def search(self, target):
    current = self.head
    while current:
        if current.data == target:
            return True
        current = current.next
    return False
```

---

### Display

```python
def display(self):
    temp = self.head
    elements = []
    while temp:
        elements.append(str(temp.data))
        temp = temp.next
    print(" -> ".join(elements) + " -> None")
```

---

## 5. Execution & Output

```
20 -> 10 -> 30 -> None
20 -> 30 -> None
Is 30 in list? True
```

---

## 6. Pointer Trace (Deleting Middle Node)

Initial:

```
20 -> 10 -> 30 -> None
```

Process:

* current = 20
* current.next = 10 (target)
* Skip node:

```
current.next = current.next.next
```

Result:

```
20 -> 30 -> None
```

---

## 7. Analysis

| Operation   | Time Complexity |
| ----------- | --------------- |
| Insert Head | O(1)            |
| Insert Tail | O(n)            |
| Delete      | O(n)            |
| Search      | O(n)            |

---

## 8. Conclusion

The Singly Linked List allows flexible memory usage and efficient insert/delete operations. However, searching requires traversal, making it less efficient than arrays for lookup operations.

---

## 9. Repository Contents

* `lab3_singly_linked_list.py`
* `README.md`

---
