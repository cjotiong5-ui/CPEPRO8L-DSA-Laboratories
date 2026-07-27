class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        # TODO: Pop and return the last item from the list. 
        # Check if empty first and raise IndexError if so.
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

def is_balanced(expression):
    stack = Stack()
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        # TODO: If char is an opening bracket, push it to stack.
        # If it is a closing bracket, pop from stack and check if it matches.
        # If stack is empty or doesn't match, return False.
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
    print(f"Is {expr1} balanced? {is_balanced(expr1)}") # Expected: True
    print(f"Is {expr2} balanced? {is_balanced(expr2)}") # Expected: False
