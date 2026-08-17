# Laboratory Activity No. 9

## Height Balancing in AVL Trees

---

## 1. Laboratory Information

| Field | Details |
|---|---|
| **Laboratory Title** | Height Balancing in AVL Trees |
| **Course Code** | CPEPRO8L |
| **Course Title** | Data Structures and Algorithms Laboratory |
| **Student Name** | Otiong, Cristan Jay N. |
| **Date Completed** | August 17, 2026 |
| **Term** | First Semester, AY 2026–2027 |

---

## 2. Introduction

In a worst-case scenario (inserting sorted data), a普通 BST degrades into a linear linked list with **O(n)** search time. **AVL Trees** are self-balancing binary search trees that maintain a height difference (balance factor) of at most **±1** across all nodes.

The **balance factor** of a node is defined as:

```
balance = height(left subtree) - height(right subtree)
```

A valid AVL tree requires every node's balance factor to be -1, 0, or +1. When an insertion causes a node to violate this constraint, the tree performs **rotations** to restore balance. There are four rotation cases:

* **LL (Left-Left):** Right rotation
* **RR (Right-Right):** Left rotation
* **LR (Left-Right):** Left rotation on left child, then right rotation
* **RL (Right-Left):** Right rotation on right child, then left rotation

---

## 3. Objectives

1. Calculate height metrics and balance factors dynamically.
2. Implement single and double rotations (LL, RR, LR, RL cases).
3. Demonstrate self-balancing tree insertions.

---

## 4. Methodology

### Right Rotation (LL Case)

Used when a node becomes left-heavy (balance > 1) and the insertion was in the left-left subtree.

```
      y                x
     / \             /   \
    x   C    →      A     y
   / \                   / \
  A   B                 B   C
```

1. Let `x = y.left` and `B = x.right`.
2. Set `x.right = y`.
3. Set `y.left = B`.
4. Update heights of `y` then `x`.
5. Return `x` as the new root.

### Left Rotation (RR Case)

Used when a node becomes right-heavy (balance < -1) and the insertion was in the right-right subtree.

```
    x                  y
   / \               /   \
  A   y      →      x     C
     / \           / \
    B   C         A   B
```

1. Let `y = x.right` and `B = y.left`.
2. Set `y.left = x`.
3. Set `x.right = B`.
4. Update heights of `x` then `y`.
5. Return `y` as the new root.

### Double Rotations

* **LR Case:** Left rotation on the left child, then right rotation on the node.
* **RL Case:** Right rotation on the right child, then left rotation on the node.

---

## 5. Source Code

[View Source Code](./lab9_avl.py)

---

## 6. Execution & Output

### Test 1: Insert [10, 20, 30] — Left Rotation (LL Case)

Inserting 10, 20, 30 in order creates a right-skewed tree that triggers a left rotation at the root.

```
After inserting 10:
Root: 10 (h=1, b=0)

After inserting 20:
Root: 10 (h=2, b=-1)
    R--- 20 (h=1, b=0)

After inserting 30:
Root: 20 (h=2, b=0)
    L--- 10 (h=1, b=0)
    R--- 30 (h=1, b=0)
```

**Rotation trace:**
1. After inserting 30, node 10 has balance = -2 (right-heavy).
2. Since 30 > 10 (right-right case), perform left rotation on node 10.
3. Node 20 becomes the new root, 10 becomes its left child, 30 remains the right child.

**Inorder:** 10 20 30

---

### Test 2: Insert [30, 20, 10] — Right Rotation (RR Case)

Inserting in descending order triggers a right rotation.

```
After inserting 30:
Root: 30 (h=1, b=0)

After inserting 20:
Root: 30 (h=2, b=1)
    L--- 20 (h=1, b=0)

After inserting 10:
Root: 20 (h=2, b=0)
    L--- 10 (h=1, b=0)
    R--- 30 (h=1, b=0)
```

**Inorder:** 10 20 30

---

### Test 3: Insert [10, 30, 20] — LR Case

Inserting 10, then 30, then 20 triggers a double rotation (left then right).

```
After inserting 10:
Root: 10 (h=1, b=0)

After inserting 30:
Root: 10 (h=2, b=-1)
    R--- 30 (h=1, b=0)

After inserting 20:
Root: 20 (h=2, b=0)
    L--- 10 (h=1, b=0)
    R--- 30 (h=1, b=0)
```

**Rotation trace:**
1. After inserting 20, node 10 has balance = -2.
2. Since 20 < 30 (right child, but 20 < 30 means left subtree of right child → RL case at node 10).
3. Right rotation on node 30: 30 moves down, 20 moves up.
4. Left rotation on node 10: 20 becomes root.

**Inorder:** 10 20 30

---

### Test 4: Insert [30, 10, 20] — RL Case

```
After inserting 30:
Root: 30 (h=1, b=0)

After inserting 10:
Root: 30 (h=2, b=1)
    L--- 10 (h=1, b=0)

After inserting 20:
Root: 20 (h=2, b=0)
    L--- 10 (h=1, b=0)
    R--- 30 (h=1, b=0)
```

**Inorder:** 10 20 30

---

## 7. Right Rotation Sequence Diagram

Given an unbalanced tree where node `y` is the root with balance factor +2:

```
Before Rotation:              After Right Rotation:

        y                            x
       / \                          / \
      x   C          →             A   y
     / \                              / \
    A   B                            B   C
```

### Step-by-Step

| Step | Action |
|---:|---|
| 1 | Set `x = y.left` (x is the left child of y) |
| 2 | Set `B = x.right` (save x's right subtree) |
| 3 | Set `x.right = y` (y becomes x's right child) |
| 4 | Set `y.left = B` (B becomes y's left child) |
| 5 | Update `y.height` = 1 + max(height(A), height(B)) |
| 6 | Update `x.height` = 1 + max(height(A), height(y)) |
| 7 | Return `x` as the new root |

**Why this works:** The BST property is preserved because A < x < B < y < C. After rotation, x is the root with A on the left and y on the right. y has B on its left and C on its right. All ordering relationships remain valid, and the tree height is reduced from 3 to 2.

---

## 8. Insertion Trace: [10, 20, 30] with Left Rotation

### Step 1: Insert 10

```
10 (balance = 0)
```

No rotation needed. Tree is balanced.

### Step 2: Insert 20

```
  10 (balance = -1)
    \
     20 (balance = 0)
```

Balance factor of 10 is -1. Within range. No rotation needed.

### Step 3: Insert 30

```
  10 (balance = -2) ← VIOLATION
    \
     20 (balance = -1)
       \
        30 (balance = 0)
```

Balance factor of 10 is **-2** (right-heavy). Since 30 > 10 and 30 > 20, this is the **RR case**.

**Left rotation is performed on node 10:**

```
      20 (balance = 0) ← NEW ROOT
     /  \
   10    30
```

After rotation, all nodes have balance factors of 0. The tree is balanced with height 2.

---

## 9. Time Complexity

| Operation | Average Case | Worst Case |
|---|---:|---:|
| Search | O(log n) | O(log n) |
| Insert | O(log n) | O(log n) |
| Delete | O(log n) | O(log n) |

The key advantage of AVL trees over普通 BSTs is the **guaranteed O(log n)** worst case. Because the tree is always balanced (height is always O(log n)), no operation can degrade to O(n).

---

## 10. Analysis

This laboratory demonstrated how AVL trees maintain balance through rotations after every insertion.

**Balance factor importance:** The balance factor is the core mechanism that detects when a tree becomes unbalanced. By checking this value after every insertion, the AVL tree can proactively fix structural problems before they affect performance.

**Rotation mechanics:** Single rotations (LL and RR) handle simple imbalance cases where the violation is in a straight line. Double rotations (LR and RL) handle zigzag cases where the imbalance spans two levels. Both types preserve the BST ordering property while reducing tree height.

**Practical trade-off:** AVL trees guarantee O(log n) operations at the cost of maintaining height information and performing rotations during insertion. In practice, the rotation overhead is minimal compared to the benefit of guaranteed logarithmic performance. This makes AVL trees ideal for read-heavy workloads where search performance is critical.

**Comparison with普通 BST:** A普通 BST inserting sorted data (10, 20, 30) produces a degenerate tree of height 3 with O(n) search. The AVL tree automatically rebalances to height 2, ensuring O(log n) search. This difference becomes dramatic with larger datasets.

---

## 11. Conclusion

This laboratory demonstrated how AVL trees use height tracking and rotations to maintain balance after every insertion. The four rotation cases (LL, RR, LR, RL) cover all possible imbalance scenarios and restore the AVL property in O(1) time per rotation. The guaranteed O(log n) worst-case performance makes AVL trees a practical choice for applications where consistent search performance is required. This activity strengthened my understanding of self-balancing data structures and the importance of maintaining structural invariants in tree-based algorithms.
