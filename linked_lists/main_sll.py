"""Singly linked list operations"""
from singly_linked_list import SLinkedList

sll = SLinkedList()
sll.print_ll()

print("Insert at head")
for ix in range(5):
    sll.insert_at_head(ix)
sll.print_ll()

print("Insert at tail")
for ix in range(5,10):
    sll.insert_at_tail(ix)
sll.print_ll()

print("Search for 6: ", sll.search(6))
print("Search for 12: ", sll.search(12))

print("Delete at head:", sll.delete_at_head())
print("Delete at head", sll.delete_at_head())
sll.print_ll()

print("Delete 0:", sll.delete(0))
sll.print_ll()
print("Delete 8:", sll.delete(8))
sll.print_ll()
print("Delete 10:", sll.delete(10))
sll.print_ll()

