# Laboratory Activity No. 7

## Recursion Tracing & Binary Search

---

## 1. Laboratory Information

| Field | Details |
|---|---|
| **Laboratory Title** | Recursion Tracing & Binary Search |
| **Course Code** | CPEPRO8L |
| **Course Title** | Data Structures and Algorithms Laboratory |
| **Student Name** | Otiong, Cristan Jay N. |
| **Date Completed** | August 17, 2026 |
| **Term** | First Semester, AY 2026–2027 |

---

## 2. Introduction

**Recursion** is a programming technique where a function calls itself to solve a problem by breaking it into smaller subproblems of the same type. Each recursive call works on a reduced portion of the input until it reaches a **base case** — the simplest form of the problem that can be solved directly without further recursion.

When a function calls itself, each call is placed on the **call stack** as a new **stack frame**. This frame stores the function's local variables, parameters, and return address. Once the base case is reached, the stack frames begin to resolve in reverse order, passing results back up through each call.

**Binary Search** is a classic algorithm that demonstrates recursion effectively. It operates on a **sorted array** by repeatedly dividing the search space in half. At each step, the algorithm compares the target value to the middle element. If they match, the search is complete. If the target is smaller, the algorithm searches the left half. If larger, it searches the right half. This divide-and-conquer approach reduces the search space logarithmically, making binary search highly efficient.

---

## 3. Objectives

1. Understand recursive execution, base cases, and how recursive calls are nested on the call stack.
2. Implement and test a recursive Binary Search algorithm in Python.
3. Compare the space complexity of iterative and recursive Binary Search implementations.

---

## 4. Methodology

The recursive Binary Search algorithm follows these steps:

1. Start with a **sorted array** and two indices: `low` (the beginning) and `high` (the end).
2. Calculate the **middle index**: `mid = (low + high) // 2`.
3. Compare `arr[mid]` with the **target** value.
4. If `arr[mid]` equals the target, **return** `mid` — the target is found.
5. If `arr[mid]` is greater than the target, recursively search the **left half** by calling the function with `high = mid - 1`.
6. If `arr[mid]` is smaller than the target, recursively search the **right half** by calling the function with `low = mid + 1`.
7. If `low > high`, the target is not in the array — return `-1`. This is the **base case**.

---

## 5. Source Code

[View Source Code](./lab7_recursive_search.py)

---

## 6. Execution & Output

The program tests the recursive binary search on a sorted array of 10 elements:

```python
data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
```

### Test Results

| Target | Expected Index | Actual Result |
|-------:|---------------:|-------------:|
|     23 |              5 |            5 |
|     56 |              7 |            7 |
|     50 |             -1 |           -1 |
|      2 |              0 |            0 |
|     91 |              9 |            9 |

### Console Output

```
Target: 23 -> Index: 5
Target: 56 -> Index: 7
Target: 50 -> Index: -1
Target: 2 -> Index: 0
Target: 91 -> Index: 9
```

All five test cases passed successfully.

---

## 7. Execution Stack Trace for Target 56

**Array:** `[2, 5, 8, 12, 16, 23, 38, 56, 72, 91]`

**Target:** `56`

### Call 1

```
recursive_binary_search(
    arr,
    low=0,
    high=9,
    target=56
)
```

- `mid = (0 + 9) // 2 = 4`
- `arr[4] = 16`
- `16 < 56`, so the target is in the **right half**
- Recurse with `low = 5`, `high = 9`

### Call 2

```
recursive_binary_search(
    arr,
    low=5,
    high=9,
    target=56
)
```

- `mid = (5 + 9) // 2 = 7`
- `arr[7] = 56`
- `56 == 56` — **target found!**
- Return `7`

The value `7` is returned from Call 2 back to Call 1, and then returned to the caller.

---

## 8. Call Stack Diagram

```
Call Stack

┌─────────────────────────────────────┐
│ recursive_binary_search             │
│ low = 0                             │
│ high = 9                            │
│ mid = 4                             │
│ arr[mid] = 16                       │
│ target = 56                         │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│ recursive_binary_search             │
│ low = 5                             │
│ high = 9                            │
│ mid = 7                             │
│ arr[mid] = 56                       │
│ target = 56                         │
│ RESULT = 7                          │
└─────────────────────────────────────┘
```

**Explanation:** The first call determines that `16 < 56` and delegates the search to the right half. The second call finds `56` at index `7` and returns `7`. This result propagates back through the first call and is ultimately returned as the final answer.

---

## 9. Base Case and Stack Overflow

A **base case** is the condition that tells a recursive function to stop calling itself. Without a base case, the function would call itself indefinitely.

In this implementation, the base case is:

```python
if low > high:
    return -1
```

When `low > high`, the search space is exhausted and the target is not present. This prevents further recursive calls.

**Why missing base cases lead to stack overflow:**

Every recursive call creates a new **stack frame** on the call stack. The call stack has a fixed maximum size (Python's default recursion limit is 1000). If there is no base case to stop the recursion, the function keeps calling itself, and each call adds another frame to the stack. Eventually, the stack runs out of space and raises a `RecursionError` (stack overflow).

For example, consider a factorial function written without a base case:

```python
def bad_factorial(n):
    return n * bad_factorial(n - 1)  # Never stops!
```

This function would call itself with `n-1`, `n-2`, `n-3`, and so on, until Python's recursion limit is exceeded. The base case (`if n == 0: return 1`) is essential to prevent this.

---

## 10. Iterative vs Recursive Space Complexity

| Implementation | Time Complexity | Space Complexity |
|---|---:|---:|
| Iterative Binary Search | O(log n) | O(1) |
| Recursive Binary Search | O(log n) | O(log n) |

Both implementations have the same **time complexity** because they perform the same number of comparisons. However, the recursive version uses **O(log n) additional space** because each recursive call adds a stack frame to the call stack. The iterative version uses only a constant amount of extra space (`low`, `high`, `mid`) regardless of the input size.

For an array of 1024 elements, recursive binary search would create at most ~10 stack frames, while iterative binary search uses only 3 variables. This difference becomes meaningful in memory-constrained environments or with very large datasets.

---

## 11. Time Complexity

### Best Case

```
O(1)
```

The target is found at the middle of the array on the first comparison.

### Average and Worst Case

```
O(log n)
```

Each recursive call halves the search space. For an array of `n` elements, the maximum number of recursive calls is `log₂(n)`. For example, an array of 1024 elements requires at most 10 calls.

### Recursive Space Complexity

```
O(log n)
```

Each recursive call adds one stack frame. The maximum depth of recursion equals the number of times the array can be halved, which is `log₂(n)`.

---

## 12. Analysis

This laboratory provided hands-on experience with recursion and its application in the Binary Search algorithm. The key observations are:

**Understanding recursion:** Recursion is not just about a function calling itself — it requires careful design of the base case and the recursive case. The base case ensures termination, while the recursive case makes progress toward the base case by reducing the problem size.

**Base case importance:** The base case `low > high` is critical. Without it, the function would continue calling itself even after the target is found or the search space is exhausted, leading to a stack overflow error. The base case acts as the stopping condition that allows the recursion to resolve.

**Binary Search efficiency:** Binary Search efficiently reduces the search space by half at each step. This logarithmic behavior means that even for large datasets, the algorithm requires very few comparisons compared to linear search, which must check every element.

**Stack frame usage:** Each recursive call creates a new stack frame on the call stack, storing the function's parameters and local state. This is why recursive Binary Search uses O(log n) auxiliary space, while the iterative version uses only O(1). While this difference is small for moderate input sizes, it is an important consideration in memory-sensitive applications.

**Practical comparison:** Iterative Binary Search is generally preferred in production code because it avoids the overhead of function calls and stack frame management. However, recursive Binary Search is easier to understand and is an excellent teaching tool for learning how recursion and the call stack work.

---

## 13. Conclusion

This laboratory demonstrated how recursion can be applied to implement Binary Search. By understanding recursive execution, base cases, and call stack behavior, I gained a clearer picture of how recursive algorithms operate under the hood. The comparison between iterative and recursive implementations highlighted the trade-off between code clarity and space efficiency. Overall, this activity strengthened my understanding of recursion, divide-and-conquer algorithms, and complexity analysis.
