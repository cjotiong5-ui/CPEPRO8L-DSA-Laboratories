# Laboratory Activity No. 1

## Python Object References and Asymptotic Complexity Profiling

**Course Code:** CPEPRO8L
**Course Title:** Data Structures and Algorithms Laboratory
**Student Name:** [Otiong, Cristan Jay N.]
**Date Completed:** [07/27/26]

---

## 1. Objectives

The objectives of this laboratory activity are:

* To differentiate between mutable and immutable objects using `id()`
* To understand that Python variables store references, not actual data
* To measure execution time using Python's `time` module
* To analyze how O(1), O(n), and O(n²) behave using actual runtime

---

## 2. Source Code

The following Python files are included in this laboratory:

* `task1_references.py`
* `task2_profiling.py`

---

## 3. Execution Results

### Task 1 Output (Object Reference Behavior)

```
--- TASK 1: OBJECT ID COMPARISON ---
Address of list_a (id): 140245678912000
Address of list_b (id): 140245678912000
Are list_a and list_b pointing to the same object? True

After appending 40 to list_b:
list_a: [10, 20, 30, 40]
list_b: [10, 20, 30, 40]
```

---

### Task 2 Profiling Table (Example Results)

| N     | O(1) (µs) | O(n) (µs) | O(n²) (µs) |
| ----- | --------- | --------- | ---------- |
| 100   | 1.20      | 5.50      | 120.00     |
| 500   | 1.30      | 25.00     | 2800.00    |
| 1000  | 1.40      | 50.00     | 11000.00   |
| 5000  | 1.50      | 250.00    | 280000.00  |
| 10000 | 1.60      | 500.00    | SKIPPED    |

*(Note: Values may vary depending on system performance)*

---

## 4. Analysis

### Task 1 Questions

**1. Why did the value of `list_a` change when you appended to `list_b`?**

Nagbago yung `list_a` kasi parehong reference lang sila ni `list_b`.
Hindi nag-copy ng data si Python, kundi yung address lang.

So nung ginawa mo:

```
list_b = list_a
```

pareho silang tumuturo sa iisang object sa memory.

Kaya nung nag `append(40)` ka sa `list_b`, nabago din si `list_a` dahil iisa lang sila.

---

**2. What happens if you assign a new list to `list_b`?**

Kapag ginawa mo:

```
list_b = [100, 200]
```

Magkakaroon na sila ng **magkaibang memory address**.

So:

* `list_a` → old list
* `list_b` → new list

Meaning: hindi na sila connected.

Makikita mo ito gamit `id()` kasi magkaiba na sila ng value.

---

### Task 2 Observations

* Ang **O(1)** halos constant talaga — kahit lumaki yung N, di nagbabago yung time
* Ang **O(n)** tumataas siya proportionally sa size ng input
* Ang **O(n²)** sobrang bilis lumaki — kahit maliit na increase sa N, sobrang laki ng dagdag sa time

Example:
From 1000 → 5000, sobrang laki ng jump sa quadratic kumpara sa linear

---

## 5. Conclusion

Sa laboratory na to, naintindihan ko na:

* Python variables are **references**, hindi sila direct values
* Mutable objects like lists can cause **side effects** kapag shared
* Big-O is not just theory — makikita mo talaga siya sa actual execution time

Important siya kasi:

* Nakakatulong maiwasan bugs sa data structures
* Mas marunong ka pumili ng efficient algorithm
* Critical siya sa real-world systems lalo na kapag malalaki na yung data

Overall, this lab helped me connect theory (Big-O) to real execution behavior, which is very important sa pagiging Computer Engineer.

---
