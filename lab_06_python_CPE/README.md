# Laboratory Activity No. 6

## Circular Queue Implementation

---

## 1. Laboratory Information

| Field | Details |
|---|---|
| **Laboratory Title** | Circular Queue Implementation |
| **Course Code** | CPEPRO8L |
| **Course Title** | Data Structures and Algorithms Laboratory |
| **Student Name** | Otiong, Cristan Jay N. |
| **Date Completed** | August 17, 2026 |
| **Term** | First Semester, AY 2026–2027 |

---

## 2. Introduction

A **Circular Queue** is a variation of the linear queue where the last position is connected back to the first position, forming a circle. This structure allows more efficient use of memory because once a position is dequeued, it can be reused for a new enqueue operation.

In a linear queue, once elements are dequeued, those positions are wasted even if the front of the queue has free space. A circular queue solves this by using **modulo arithmetic** (`%`) to wrap the `head` and `tail` indices around the array, effectively reusing空位 positions.

---

## 3. Objectives

1. Implement a `CircularQueue` class with `enqueue`, `dequeue`, and `display` operations.
2. Understand how modulo arithmetic enables circular index wrapping.
3. Observe overflow and underflow conditions in a fixed-capacity queue.

---

## 4. Methodology

The circular queue works as follows:

1. Initialize a fixed-size array with `None` values, along with `head`, `tail`, and `size` indicators.
2. **Enqueue:** Insert the item at the current `tail` position, then update `tail = (tail + 1) % capacity`. Increment `size`.
3. **Dequeue:** Retrieve the item at the current `head` position, set it to `None`, then update `head = (head + 1) % capacity`. Decrement `size`.
4. **Overflow check:** If `size == capacity`, the queue is full and cannot accept new items.
5. **Underflow check:** If `size == 0`, the queue is empty and cannot dequeue.

The modulo operation ensures that when `head` or `tail` reaches the end of the array, it wraps back to index `0`.

---

## 5. Source Code

[View Source Code](./lab6_circular_queue.py)

---

## 6. Execution & Output

The program creates a circular queue with capacity 5 and performs the following operations:

1. Enqueue `1`, `2`, `3`
2. Dequeue one element (returns `1`)
3. Enqueue `4`
4. Display the queue state

### Console Output

```
Dequeued: 1
Queue array: [None, 2, 3, 4, None] | Head: 1 | Tail: 4
```

### Step-by-Step Trace

| Operation | Queue State | Head | Tail | Size |
|---|---|---:|---:|---:|
| `enqueue(1)` | `[1, None, None, None, None]` | 0 | 1 | 1 |
| `enqueue(2)` | `[1, 2, None, None, None]` | 0 | 2 | 2 |
| `enqueue(3)` | `[1, 2, 3, None, None]` | 0 | 3 | 3 |
| `dequeue()` → `1` | `[None, 2, 3, None, None]` | 1 | 3 | 2 |
| `enqueue(4)` | `[None, 2, 3, 4, None]` | 1 | 4 | 3 |

After dequeuing `1`, the head position moves from `0` to `1`. The freed slot at index `0` remains empty, but future enqueue operations will eventually wrap around and reuse it.

---

## 7. Analysis

### Circular vs Linear Queue

| Feature | Linear Queue | Circular Queue |
|---|---|---|
| Index movement | Only forward | Wraps around using modulo |
| Memory reuse | Wasted after dequeue | Reuses freed positions |
| Overflow detection | Tail reaches end | `size == capacity` |

### Time Complexity

| Operation | Complexity |
|---|---:|
| `enqueue` | O(1) |
| `dequeue` | O(1) |
| `is_full` / `is_empty` | O(1) |
| `display` | O(n) |

All primary operations execute in constant time because they involve direct index access and arithmetic.

### Key Observations

- The modulo operation `(index + 1) % capacity` is what makes the queue circular. Without it, the indices would only increase linearly.
- The `size` variable simplifies overflow and underflow detection. An alternative approach uses a single empty slot to distinguish between full and empty states, but tracking `size` is more straightforward.
- When the queue is not full, there is always a contiguous block of `None` values between `tail` and `head` (wrapping around), representing available space.

---

## 8. Conclusion

This laboratory demonstrated how a Circular Queue reuses memory by wrapping indices with modulo arithmetic. Unlike a linear queue where dequeued positions are wasted, the circular design allows those positions to be reclaimed for future enqueue operations. The implementation achieved O(1) time complexity for both enqueue and dequeue, making it efficient for scenarios with frequent insertions and removals such as scheduling, buffering, and resource management.
