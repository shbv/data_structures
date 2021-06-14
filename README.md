# Linear data structures:
- Lists:           O(n) insert/deletes           ; O(1) random access (amortized O(1) to insert/delete element from end)
- Linked lists:    O(1) insert/deletes at head   ; O(n) random access (O(n) to insert/delete at tail for single linked list)
- Stacks:          O(1) insert/deletes
- Queues:          O(1) insert, O(n) delete

# Non-linear data structures:
- Graphs: (reference: educative.io)
		Operation			Adjacency List	    Adjacency Matrix
		Add Vertex			     O(1)		O(V^2)
		Remove Vertex			     O(V+E)		O(V^2)
		Add Edge			     O(1)		O(1)
		Remove Edge			     O(E)		O(1)
		Search				     O(V)		O(1)
		Breadth First Search(BFS)	     O(V+E)		O(V^2)
		Depth First Search(DFS)		     O(V+E)		O(V^2)	
- 
 
