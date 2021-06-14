"""
Double ended queue: Add or remove elements from both ends 
    - O(n) random access time unlike lists due to doubly linked list backend
"""

from collections import deque


""" 
Stack 
"""
s = deque()
print(f"stack: {s}")

l = list(range(3))

print(f"==Push elements {l} into stack==")
for el in l:
    s.append(el)
print(f"stack: {s}")

print(f"==Pop elements from stack==")
for _ in range(len(l)):
    print(f"{s.pop()}")
print(f"stack: {s}")


"""
Queue 
"""
s = deque()
print(f"queue: {s}")

l = list(range(3))

print(f"==Enqueue elements {l} into stack==")
for el in l:
    s.append(el)
print(f"queue: {s}")

print(f"==Dequeue elements from stack==")
for _ in range(len(l)):
    print(f"{s.popleft()}")
print(f"queue: {s}")

