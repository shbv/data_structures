"""
Custom class for queue (FIFO) using lists
    - Delete elements from front of queue
    - Add elements to back (rear) of queue

Usage examples:
    - caching / storing info (process info, packets, etc) in common resource shared across devices 

Types of queues:
    - Linear: basic
    - Circular: front & rear are connected
    - Priority: elements have priority & are sorted. highest priority is on front. (e.g. OS process priority)
    - Double-ended: queue from both ends, so enqueue/dequeue work on both ends
"""

class MyQueue:
    def __init__(self):
        self.queue_list = []
        self.queue_size = 0

    def is_empty(self):
        return self.queue_size == 0

    def size(self):
        return self.queue_size

    def front(self):
        if self.is_empty(): return None
        return self.queue_list[0]

    def rear(self):
        if self.is_empty(): return None
        return self.queue_list[-1]

    def enqueue(self, element):
        self.queue_size += 1
        self.queue_list.append(element)

    # O(n) using list
    def dequeue(self):
        if self.is_empty(): return None
        front = self.front()
        self.queue_list.remove(front)
        self.queue_size -= 1
        return front

if __name__ == '__main__':

    s = MyQueue()
    print(f"is_empty: {s.is_empty()}, size: {s.size()}, front(): {s.front()}, rear(): {s.rear()}, dequeue: {s.dequeue()}")

    l = list(range(3))
    
    print(f"==Enqueue elements {l} into queue==")
    for el in l:
        s.enqueue(el)
    print(f"is_empty: {s.is_empty()}, size: {s.size()}, front(): {s.front()}, rear(): {s.rear()}")

    print(f"==Dequeue elements from queue==")
    for _ in range(len(l)):
        print(f"{s.dequeue()}")
    print(f"is_empty: {s.is_empty()}, size: {s.size()}, front(): {s.front()}, rear(): {s.rear()}, dequeue: {s.dequeue()}")
    
