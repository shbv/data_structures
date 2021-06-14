"""
Graph components:
    - Nodes/Vertices (number denoted by n or V)
    - Edges with/without weights/direction  (number denoted by E)

Some terms:
    - Degree (in/out) of vertex: number of edges on it
    - Adjacent vertices:  connected by edge
    - Self loop: edge with start & end on same vertex

Some types:
    - Undirected:       No directed edges. n(n-1)/2 max edges
    - Directed:         Directed edges. n(n-2) max edges
    - Cyclic:           Traversal => revisit vertex
    - Bi(k)-partite:    2 (k=2) sets of vertices. No edges between vertices within the same set. (Vertices within same set are not adjacent)

Representation: 
    - Adjacency matrix:  
        - O(V^2) size.  
        - 2-d matrix with 0/1 if edge exists
        - Efficient for apps that manipulate edges
    - Adjacenct list:    
        - O(V)   size.  
        - Array of linked lists with neighbor nodes/vertices
        - Efficient for apps that manipulate vertices

Complexity: (reference: educative.io)
	Operation			Adjacency List	    Adjacency Matrix
	Add Vertex			     O(1)		O(V^2)
	Remove Vertex			     O(V+E)		O(V^2)
	Add Edge			     O(1)		O(1)
	Remove Edge			     O(E)		O(1)
	Search				     O(V)		O(1)
	Breadth First Search(BFS)	     O(V+E)		O(V^2)
	Depth First Search(DFS)		     O(V+E)		O(V^2)	
    
Usage:
    - Networks (neural/p2p/social), etc.
    
"""
from singly_linked_list import SLinkedList

class Graph:
    """
    Directed graph with adjacency list representation (List of linked lists)
    """

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = []
        for ix in range(self.num_vertices):
            self.adj_list.append(SLinkedList())

    def print_graph(self):
        for ix in range(self.num_vertices):
            print(f"{ix}", end=" => ")
            self.adj_list[ix].print_ll()
            
    def add_edge(self, source_vertex, destination_vertex):
        if (source_vertex < self.num_vertices and destination_vertex < num_vertices):
            self.adj_list[source_vertex].insert_at_head(destination_vertex)
            #self.adj_list[destination_vertex].insert_at_head(source_vertex) #for undirected graphs


if __name__ == '__main__':
    
    num_vertices = 3
    g = Graph(num_vertices)

    print("== Empty graph ==")
    g.print_graph()

    edges = [(1,2), (0,2), (0,1)]
    print(f"== Add edges {edges} ==")
    for e in edges:
        g.add_edge(*e)
    g.print_graph()




