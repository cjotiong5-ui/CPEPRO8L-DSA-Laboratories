# Laboratory Activity No. 8

## Binary Search Tree Insertion and Traversals

---

## 1. Laboratory Information

| Field | Details |
|---|---|
| **Laboratory Title** | Binary Search Tree Insertion and Traversals |
| **Course Code** | CPEPRO8L |
| **Course Title** | Data Structures and Algorithms Laboratory |
| **Student Name** | Otiong, Cristan Jay N. |
| **Date Completed** | August 17, 2026 |
| **Term** | First Semester, AY 2026–2027 |

---

## 2. Introduction

A **Binary Search Tree (BST)** is a hierarchical non-linear data structure where each node has at most two children: a left child and a right child. The BST property states that for any given node:

* All elements in the **left subtree** are smaller than the node's key.
* All elements in the **right subtree** are greater than the node's key.

This ordering property allows search, insertion, and deletion operations to execute in **O(log n)** average time, because each comparison eliminates roughly half of the remaining nodes. In the worst case (a degenerate/skewed tree), these operations degrade to **O(n)**.

Tree traversals visit every node in a specific order. The three standard depth-first traversals are:

* **Inorder** (Left → Node → Right): Produces sorted output for a BST.
* **Preorder** (Node → Left → Right): Useful for copying/serializing a tree.
* **Postorder** (Left → Right → Node): Useful for deleting a tree.

---

## 3. Objectives

1. Implement dynamic tree nodes with left and right child references.
2. Build insertion and lookup functions in a Binary Search Tree.
3. Implement Inorder, Preorder, and Postorder recursive tree traversals.

---

## 4. Methodology

### Insertion

1. If the tree is empty, create a new `TreeNode` and set it as the root.
2. Otherwise, compare the new key with the current node's key.
3. If the key is **smaller**, move to the **left** child.
4. If the key is **greater or equal**, move to the **right** child.
5. When an empty position (`None`) is reached, insert the new node there.

### Traversals

* **Inorder:** Recursively traverse the left subtree, visit the current node, then recursively traverse the right subtree.
* **Preorder:** Visit the current node, recursively traverse the left subtree, then recursively traverse the right subtree.
* **Postorder:** Recursively traverse the left subtree, recursively traverse the right subtree, then visit the current node.

---

## 5. Source Code

[View Source Code](./lab8_bst.py)

---

## 6. Execution & Output

The program builds a BST from the elements `[50, 30, 70, 20, 40, 60, 80]` and prints all three traversals.

### Tree Structure

```
        50
       /  \
      30    70
     / \   / \
    20  40 60  80
```

### Console Output

```
Inorder Traversal:
20 30 40 50 60 70 80
Preorder Traversal:
50 30 20 40 70 60 80
Postorder Traversal:
20 40 30 60 80 70 50
```

### Traversal Results Summary

| Traversal | Order | Output |
|---|---|---|
| Inorder | Left → Node → Right | 20 30 40 50 60 70 80 |
| Preorder | Node → Left → Right | 50 30 20 40 70 60 80 |
| Postorder | Left → Right → Node | 20 40 30 60 80 70 50 |

---

## 7. Insertion Trace

The following shows how each element is inserted into the tree:

| Step | Element | Action |
|---:|---:|---|
| 1 | 50 | Tree is empty — 50 becomes the root. |
| 2 | 30 | 30 < 50 — inserted as left child of 50. |
| 3 | 70 | 70 > 50 — inserted as right child of 50. |
| 4 | 20 | 20 < 50 → 20 < 30 — inserted as left child of 30. |
| 5 | 40 | 40 < 50 → 40 > 30 — inserted as right child of 30. |
| 6 | 60 | 60 > 50 → 60 < 70 — inserted as left child of 70. |
| 7 | 80 | 80 > 50 → 80 > 70 — inserted as right child of 70. |

---

## 8. Report Analysis Questions

### Preorder and Postorder Outputs

**Preorder output:** `50 30 20 40 70 60 80`

The preorder traversal visits the root first (50), then recursively processes the left subtree (30, 20, 40), and finally the right subtree (70, 60, 80). This order is useful for creating a copy of the tree because it preserves the structure — reading preorder output and inserting in the same order reconstructs the identical tree.

**Postorder output:** `20 40 30 60 80 70 50`

The postorder traversal visits children before the parent. It processes the left subtree (20, 40, 30), then the right subtree (60, 80, 70), and finally the root (50). This order is useful for deleting a tree because you can safely delete a node after its children have been removed.

### Why Inorder Traversal Produces Sorted Order

The inorder traversal follows the **Left → Node → Right** pattern. Because of the BST property:

* Every node in the **left subtree** has a key **smaller** than the current node.
* Every node in the **right subtree** has a key **greater** than the current node.

When we traverse left first, we visit all smaller values before the current node. Then we visit the current node. Then we traverse right, visiting all larger values. Since this pattern is applied recursively at every level of the tree, the result is a fully sorted sequence.

For example, at the root (50):
1. The entire left subtree (20, 30, 40) is visited first — all values less than 50.
2. Then 50 itself is visited.
3. Then the entire right subtree (60, 70, 80) is visited — all values greater than 50.

This recursive structure guarantees that the inorder output is always in ascending sorted order for any valid BST.

---

## 9. Time Complexity

| Operation | Average Case | Worst Case |
|---|---:|---:|
| Insertion | O(log n) | O(n) |
| Inorder Traversal | O(n) | O(n) |
| Preorder Traversal | O(n) | O(n) |
| Postorder Traversal | O(n) | O(n) |

* **Average case** assumes a balanced tree where each level is roughly half full.
* **Worst case** occurs when elements are inserted in sorted order, producing a skewed (degenerate) tree that behaves like a linked list.

---

## 10. Analysis

This laboratory provided hands-on experience with Binary Search Tree operations. The key observations are:

**BST property:** The ordering invariant (left < node < right) is what makes the BST efficient. Every insertion decision reduces the search space by half on average, similar to binary search on a sorted array. However, unlike an array, a BST allows efficient insertion without shifting elements.

**Recursive nature of BST operations:** Both insertion and traversal are naturally recursive. Insertion follows a single path from root to leaf (O(log n) average), while traversals visit every node (O(n)). The recursive structure mirrors the tree's own hierarchical structure, making the code clean and intuitive.

**Traversal differences:** Each traversal serves a different purpose. Inorder produces sorted output and is useful for validation. Preorder preserves the tree structure for serialization. Postorder is ideal for safe deletion. Understanding when to use each traversal is important for practical tree-based algorithms.

**Balanced vs skewed trees:** The efficiency of BST operations depends heavily on the tree's shape. Inserting elements in random order typically produces a reasonably balanced tree. However, inserting already-sorted data (e.g., 20, 30, 40, 50, 60, 70, 80) creates a degenerate tree with O(n) operations. This limitation motivates the study of self-balancing trees such as AVL trees and Red-Black trees in more advanced courses.

---

## 11. Conclusion

This laboratory demonstrated how a Binary Search Tree organizes data hierarchically while maintaining sorted order through the BST property. The recursive implementations of insertion and the three traversal methods (Inorder, Preorder, Postorder) showed how recursion naturally maps to tree structures. The Inorder traversal's ability to produce sorted output confirmed the correctness of the BST property. Overall, this activity strengthened my understanding of non-linear data structures and recursive algorithms.
