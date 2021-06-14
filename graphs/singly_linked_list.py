from snode import SNode

class SLinkedList:
    """Singly Linked List"""

    def __init__(self):
        self.head_node = None

    # O(1) comp
    def get_head(self):
        return self.head_node

    # O(1) 
    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False
    
    # O(1) 
    def insert_at_head(self, data):
        node = SNode(data)
        node.next = self.head_node
        self.head_node = node
        return self.head_node
    
    # O(n)
    def insert_at_tail(self, data):
        node = SNode(data)
        if self.head_node is None:
            self.head_node = node
            return
        curr_node = self.head_node
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node

    # O(n)
    def search(self, data):
        curr_node = self.head_node
        while curr_node is not None:
            if curr_node.data == data:
                return True
            curr_node = curr_node.next
        return False

    # O(1)
    def delete_at_head(self):
        curr_head = self.head_node
        if curr_head is None: return False
        self.head_node = curr_head.next
        curr_head.next = None
        return True

    # O(n)
    def delete(self, data):
        if self.head_node is None:
            return False

        prev_node = None
        curr_node = self.head_node
        if curr_node.data == data:
            # delete 1st node
            self.delete_at_head()
            return True
        while curr_node is not None:
            if curr_node.data == data:
                # delete curr_node
                prev_node.next = curr_node.next
                curr_node.next = None
                return True
            prev_node = curr_node
            curr_node = curr_node.next
        return False

    def print_ll(self):
        if self.is_empty(): 
            #print("LL is empty")
            print("None")
            return
        #print("sll head =", self.head_node.data)
        #print("sll =", end=" ")
        curr_node = self.head_node
        while curr_node.next is not None:
            print(curr_node.data, end=" -> ")
            curr_node = curr_node.next
        print(curr_node.data, "-> None")

