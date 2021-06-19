"""
Tree components:
    - Nodes/Vertices (n/V)
    - Edges
    - One path between nodes (acyclic graphs)

Terms:
    - root (optional), parent, child, sibling, leaf, ancestor nodes, sub-tree
    - search path in binary tree: sequence of nodes from root to node
    - length of path: number of edges in path 
    - degree of node: number of child nodes
    - depth of node: path length from node to root. (number of edges, or number of nodes excluding itself)
    - level of node: depth+1
    - height of node: path length from node to leaf, i.e., deepest descendent. (number of edges, or number of nodes excluding itself)
    - height of tree (h): height of root 
    - balanced tree: abs(height of left-sub-tree - height of right-sub-tree) <= 1 for all nodes

Types:
    - Bin(k)-ary tree: Each node has atmost k=2 child nodes
        - Perfect: Full & Complete. 
            - 2^(h+1)-1 nodes (= 2^0 + 2^1 + 2^2 + ...), 2^h leaf nodes.
        - Complete: All levels are fully filled except maybe last level (filled left to right)
            - >= (2^h) nodes, <= 2^(h+1)-1 nodes
        - Full/Proper: Every node has 0 or 2 children. No 1 child.  
            - >= (2h+1) nodes, <= 2^(h+1)-1 nodes. 
        - Skewed: All nodes, except leaf, have only 1 child 
    - Binary search tree
        - Each node has (key, value) pairs.  
        - Ordered tree: key(left-sub-tree) < key(node) < key(right-sub-tree)
        - O(h) insertion/deletion/search. 0(n) in worst case - skewed BST. O(logn) in bestcase - AVL tree
    - AVL tree
        - BST + balanced tree 
        - h = O(logn). O(logn) insertion/deletion/search.
        - More balanced (but more rotations during insertion/deletion) than Red-Black tree. Useful for search-intensive apps
    - Red-Black tree
        - BST + Nodes are black/red
        - Root, None nodes: black. Parent/child nodes cannot be both red (i.e. not adjacent)
        - Number of black nodes from Root to None is same for all paths
        - h <= 2log(n+1). O(logn) insertion/deletion/search.
    - 2-3 tree
        - Not BST. Balanced: All leaf nodes at same level.
        - Ordered tree with 2/3 child nodes: 
            - 2-child node (1 key): key(left-sub-tree) < key(node) < key(right-sub-tree)
            - 3-child node (2 keys): key(left-sub-tree) < key1(node) < key(mid-sub-tree) < key2(node) < key(right-sub-tree)
        - h < log(n+1). O(logn) insertion/deletion/search.
"""
