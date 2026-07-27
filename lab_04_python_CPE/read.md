# 📘 Laboratory Activity No. 4

## Doubly and Circular Linked Lists

---

## 1. 🧾 Laboratory Information

* **Laboratory Title:** Doubly and Circular Linked Lists
* **Course Code:** CPEPRO8L
* **Student Name:** *[Your Name Here]*
* **Date Completed:** *[Insert Date]*

---

## 2. 🎯 Objectives

* To implement a **Doubly Linked List** using `next` and `prev` pointers
* To build a **Circular Singly Linked List** with proper looping structure
* To understand the difference between **linear traversal** and **circular traversal**

---

## 3. 💻 Source Code

The following Python file is included in this laboratory:

```
lab4_doubly_circular.py
```

---

## 4. ▶️ Execution Results

### 🔹 Doubly Linked List Output

```
--- Testing Doubly Linked List ---
None <-> 10 <-> 5 <-> None
```

### 🔹 Circular Linked List Output

```
--- Testing Circular Linked List ---
100 -> 200 -> 300 -> (loops to 100)
```

📌 *Note:*
You can also attach screenshots here if required by your instructor.

---

## 5. 🧪 Analysis

### ✅ Program Completion

Na-complete successfully yung required methods:

* `insert_head()` for Doubly Linked List
* `insert_tail()` for Circular Linked List
* `display()` functions for both

Walang errors during execution and tama yung output based sa expected result.

---

### 🔁 Traversal Termination in Circular Linked List

Sa **Circular Linked List**, walang `None` sa dulo kasi yung last node ay bumabalik sa **head**.

👉 Problem:
Kapag gumamit ka ng normal loop tulad nito:

```
while temp != None:
```

magiging **infinite loop** siya.

👉 Solution:
Kailangan mong i-stop yung traversal kapag bumalik ka na ulit sa head:

```
start = self.head
temp = self.head

while True:
    temp = temp.next
    if temp == start:
        break
```

💡 Explanation (simple lang):

* Start ka sa head
* Traverse mo lahat ng nodes
* Stop kapag umikot ka na pabalik sa simula

---

## 6. 🧠 Conclusion

Sa lab na to, natutunan ko yung difference ng dalawang linked list structures:

* **Doubly Linked List**

  * May `prev` at `next`
  * Pwede mag forward at backward traversal
* **Circular Linked List**

  * Walang end (`None`)
  * Tuloy-tuloy yung loop

📌 Important learnings:

* Pointers are very important sa data structures
* Kailangan careful sa traversal lalo na sa circular lists
* Na-improve yung understanding ko sa memory linking and node connections

Overall, helpful yung lab kasi mas naging clear kung paano gumagana internally yung linked lists and paano sila ginagamit sa real applications.

---
