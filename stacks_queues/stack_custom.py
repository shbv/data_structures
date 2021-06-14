"""
Custom class for stack (LIFO) using lists
    - pop elements from top of stack

Usage examples:
    - Backtracking or store info for partially completed task (stack dump, recursion, graph traversal, etc.)
"""

class MyStack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0

    def is_empty(self):
        return self.stack_size == 0

    def size(self):
        return self.stack_size

    def peek(self):
        if self.is_empty(): return None
        return self.stack_list[-1]

    def push(self, element):
        self.stack_size += 1
        self.stack_list.append(element)

    def pop(self):
        if self.is_empty(): return None
        self.stack_size -= 1
        return self.stack_list.pop()

if __name__ == '__main__':

    s = MyStack()
    print(f"is_empty: {s.is_empty()}, size: {s.size()}, peek(): {s.peek()}, pop: {s.pop()}")

    l = list(range(3))
    
    print(f"==Push elements {l} into stack==")
    for el in l:
        s.push(el)
    print(f"is_empty: {s.is_empty()}, size: {s.size()}, peek(): {s.peek()}")

    print(f"==Pop elements from stack==")
    for _ in range(len(l)):
        print(f"{s.pop()}")
    print(f"is_empty: {s.is_empty()}, size: {s.size()}, peek(): {s.peek()}, pop: {s.pop()}")
    
