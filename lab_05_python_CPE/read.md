# 📘 Laboratory Documentation: Stack Implementation & Balanced Brackets

---

## 1. Laboratory Information

| **Field**          | **Details**                               |
| ------------------ | ----------------------------------------- |
| **Course Code**    | CPEPRO8L                                  |
| **Course Title**   | Data Structures and Algorithms Laboratory |
| **Student Name**   | Otiong, Cristan Jay N.                    |
| **Date Completed** | July 16, 2026                             |
| **Term**           | First Semester, AY 2026–2027              |

---

## 2. Objectives

The objectives of this laboratory are:

* To understand the concept of **Stack data structure**
* To implement basic stack operations such as push, pop, and peek
* To apply stack in solving problems involving expressions
* To create a program that checks if brackets in an expression are balanced

---

## 3. Source Code

The following Python file is included in this laboratory:

* `stack_balanced.py`

```python
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

def is_balanced(expression):
    stack = Stack()
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty():
                return False
            if stack.pop() != bracket_map[char]:
                return False

    return stack.is_empty()

if __name__ == "__main__":
    expr1 = "{[()()]}"
    expr2 = "{[(])}"
    print(f"Is {expr1} balanced? {is_balanced(expr1)}")
    print(f"Is {expr2} balanced? {is_balanced(expr2)}")
```

---

## 4. Execution Results

### Console Output

```
Is {[()()]} balanced? True
Is {[(])} balanced? False
```

### Explanation

* `{[()()]}` is balanced because all brackets are properly matched and nested
* `{[(])}` is not balanced due to incorrect pairing of brackets

---

## 5. Analysis

This program uses a **Stack**, which follows the **Last In, First Out (LIFO)** principle.

* Opening brackets are pushed into the stack
* Closing brackets trigger a pop operation
* The popped value is compared with the expected opening bracket
* If there is a mismatch or the stack is empty, the expression is invalid

This ensures that both **order and pairing of brackets** are correct.

---

## 6. Conclusion

In this laboratory, I learned how to implement a Stack data structure and apply it to solve a real problem. I gained a better understanding of how stack operations work and how they are used in validating expressions.

This activity improved my skills in problem solving and algorithm design. It also showed the importance of choosing the right data structure for efficient program execution.

Overall, this laboratory helped strengthen my foundation in Data Structures and Algorithms.
