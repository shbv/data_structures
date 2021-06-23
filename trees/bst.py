"""
Binary search tree custom code
"""
import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left, self.right, self.parent = None, None, None

    # insert recursive 
    def insert_node_in_subtree(self, value):
        if value < self.value:
            if self.left is not None:
                self.left.insert_node_in_subtree(value)
            else:
                self.left = Node(value)
        else:
            if self.right is not None:
                self.right.insert_node_in_subtree(value)
            else:
                self.right = Node(value)

    # insert iterative 
    def insert_node_in_subtree_iterative(self, value):
        curr_node = self
        while curr_node is not None:
            if value < curr_node.value:
                if curr_node.left is not None:
                    curr_node = curr_node.left
                else:
                    curr_node.left = Node(value)
                    break
            else:
                if curr_node.right is not None:
                    curr_node = curr_node.right
                else:
                    curr_node.right = Node(value)
                    break
                
    # search recursive
    def search_node_in_subtree(self, value):
        if self.value == value:
            return True
        if value < self.value:
            if self.left is not None:
                return self.left.search_node_in_subtree(value)
            else:
                return False
        else:
            if self.right is not None:
                return self.right.search_node_in_subtree(value)
            else:
                return False

    # delete recursive
    def delete_node_in_subtree(self, value):
        
        # found node
        if self.value == value:
            print(f"Found node with {value}, deleting ..")
            if self.left is None and self.right is None:
                self = None
                return None
            elif self.left is None:
                right_child_node = self.right
                self = None
                return right_child_node
            elif self.right is None:
                left_child_node = self.left
                self = None
                return left_child_node
            else:
                # traverse right subtree, find a node & insert its value in self, delete the found node
                curr_node = self.right
                while curr_node is not None:
                    curr_node = curr_node.left
                self.value = curr_node.value
                self.right = self.right.delete_node_in_subtree(curr_node.value)
        
        # search for node
        if value < self.value:
            if self.left is not None:
                self.left = self.left.delete_node_in_subtree(value)
            else:
                print(f"Reached leaf, could not find {value} in BST")
        else:
            if self.right is not None:
                self.right = self.right.delete_node_in_subtree(value)
            else:
                print(f"Reached leaf, could not find {value} in BST")
        return self
    

class BST:
    def __init__(self, root_value):
        self.root = Node(root_value)
    
    def insert(self, value):
        if self.root is not None:
            self.root.insert_node_in_subtree(value)
        else:
            self.root = Node(value)

    def insert_iterative(self, value):
        if self.root is not None:
            self.root.insert_node_in_subtree_iterative(value)
        else:
            self.root = Node(value)

    def search(self, value):
        if self.root is not None:
            return self.root.search_node_in_subtree(value)
        else:
            return False

    def delete(self, value):
        if self.root is not None:
            self.root = self.root.delete_node_in_subtree(value)
        else:
            print("BST is empty")

    def print_preorder(self, node):
        if node is not None:
            print(node.value)
            self.print_preorder(node.left)
            self.print_preorder(node.right)

    def print_postorder(self, node):
        if node is not None:
            self.print_postorder(node.left)
            self.print_postorder(node.right)
            print(node.value)

    def print_inorder(self, node):
        if node is not None:
            self.print_inorder(node.left)
            print(node.value)
            self.print_inorder(node.right)

if __name__ == "__main__":
    
    elem = 50
    print(f"== Creating BST with root node value: {elem} ==") 
    bst = BST(elem)
    print(f"== Preorder print ==") 
    bst.print_preorder(bst.root)
    #arr = random.sample(range(0, 100), 6)
    arr = [59, 3, 91, 8, 63, 0]
    print(f"inserting nodes with values: {arr} using recursive code ==") 
    for elem in arr:
        bst.insert(elem)
    print(f"== Preorder print ==") 
    bst.print_preorder(bst.root)

    elem = 50
    print(f"== Creating BST with root node value: {elem} ==") 
    bst = BST(elem)
    print(f"== Preorder print ==") 
    bst.print_preorder(bst.root)
    print(f"inserting nodes with values: {arr} using iterative code ==") 
    for elem in arr:
        bst.insert_iterative(elem)
    print(f"== Preorder print ==") 
    bst.print_preorder(bst.root)
    print(f"== Postorder print ==") 
    bst.print_postorder(bst.root)
    print(f"== inorder print ==") 
    bst.print_inorder(bst.root)
    
    elem = 91
    print(f"Search BST for {elem}: { bst.search(elem) }") 
    elem = 9
    print(f"Search BST for {elem}: { bst.search(elem) }") 

    elem = 91
    print(f"== Delete {elem}: ==") 
    bst.delete(elem)
    elem = 9
    print(f"== Delete {elem}: ==") 
    bst.delete(elem)
    print(f"== Preorder print ==") 
    bst.print_preorder(bst.root)

