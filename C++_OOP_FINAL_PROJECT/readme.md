
Graph via Adjacency Lists - Explanation and Implementation
Overview
This program implements graph representations using adjacency lists through dynamic arrays in C++. It supports both directed and undirected graphs using an abstract base class and polymorphism. Users can input multiple graphs, add edges, and view the graph structure using pointer arithmetic.

1. Structures Used
- Edge: Holds destination vertex ID and edge weight.
- Vertex: Holds vertex ID, a dynamic array of Edges, and a count of how many edges.
- These structures form the foundation for representing adjacency lists.

2. Abstract Base Class: Graph
- Holds dynamic array of Vertex.
- Provides virtual function addEdge() for edge addition.
- Contains methods to add, remove, and find vertices.
- Uses pointer arithmetic for array access.
- Provides a virtual printGraph() method.

3. Derived Classes: DirectedGraph and UndirectedGraph
- DirectedGraph: Adds a one-way edge from 'from' to 'to'.
- UndirectedGraph: Adds two edges, one in each direction.
- Each class overrides addEdge() and printGraph().
- Uses pointer arithmetic to insert new edges.

4. Main Function
- Accepts number of graphs from the user.
- Lets user select graph type for each.
- Accepts edges for each graph.
- Demonstrates runtime polymorphism using Graph** array.
- Outputs graph contents and deallocates memory.

5. Key C++ Concepts Demonstrated
- Dynamic memory allocation and deallocation
- Pointer arithmetic for array navigation
- Abstract classes and inheritance
- Runtime polymorphism
- Encapsulation and modular design
- Graph theory principles (adjacency list)

6. Program Output Example
Example Input:
2
1
3
0 1 2.5
1 2 3.5
2 0 1.5
2
2
3 4 1.2
4 3 2.3

Output:
Directed Graph:
Vertex 0 -> (1, 2.5) 
Vertex 1 -> (2, 3.5) 
Vertex 2 -> (0, 1.5) 

Undirected Graph:
Vertex 3 -> (4, 1.2) 
Vertex 4 -> (3, 2.3) 

Detailed screenshot showing how the system work

![Screenshot 2025-06-19 115738](https://github.com/user-attachments/assets/60e8350d-755b-477a-beba-1d77f9b026cf)
![Screenshot 2025-06-19 115712](https://github.com/user-attachments/assets/543d4342-1d5d-470c-b4a3-8ef14f283612)
![Screenshot 2025-06-19 115656](https://github.com/user-attachments/assets/0cf325fb-75ad-4f75-8983-4d3f70d120a9)
![Screenshot 2025-06-19 115635](https://github.com/user-attachments/assets/026c4abc-5290-470b-b830-05b1d05e9359)


7. Conclusion
This project demonstrates advanced object-oriented programming in C++ to simulate real-world graph structures. It uses inheritance and dynamic memory to create scalable and flexible solutions for directed and undirected graphs.

