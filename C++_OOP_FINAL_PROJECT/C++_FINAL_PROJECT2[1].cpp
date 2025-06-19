// Graph via Adjacency Lists - C++ OOP Implementation

#include <iostream>
using namespace std;

struct Edge {
    int to;
    float weight;
};

struct Vertex {
    int id;
    Edge* edges;
    int edgeCount;

   Vertex() : id(-1), edges(NULL), edgeCount(0) {}

    void addEdge(int to, float weight) {
        Edge* temp = new Edge[edgeCount + 1];
        for (int i = 0; i < edgeCount; ++i) temp[i] = edges[i];
        temp[edgeCount] = {to, weight};
        delete[] edges;
        edges = temp;
        ++edgeCount;
    }

    void showEdges() {
        cout << "Vertex " << id << " has edges:\n";
        for (int i = 0; i < edgeCount; ++i) {
            Edge* e = edges + i; // pointer arithmetic
            cout << "  -> To: " << e->to << ", Weight: " << e->weight << endl;
        }
    }

    ~Vertex() {
        delete[] edges;
    }
};

class Graph {
protected:
    Vertex* vertices;
    int vertexCount;
public:
    Graph() : vertices(nullptr), vertexCount(0) {}

    virtual void addEdge(int from, int to, float weight) = 0;

    virtual void addVertex(int id) {
        Vertex* temp = new Vertex[vertexCount + 1];
        for (int i = 0; i < vertexCount; ++i) temp[i] = vertices[i];
        temp[vertexCount].id = id;
        delete[] vertices;
        vertices = temp;
        ++vertexCount;
    }

    virtual void removeVertex(int id) {
        int index = -1;
        for (int i = 0; i < vertexCount; ++i) {
            if (vertices[i].id == id) index = i;
        }
        if (index == -1) return;
        Vertex* temp = new Vertex[vertexCount - 1];
        for (int i = 0, j = 0; i < vertexCount; ++i) {
            if (i != index) temp[j++] = vertices[i];
        }
        delete[] vertices;
        vertices = temp;
        --vertexCount;
    }

    virtual void display() {
        for (int i = 0; i < vertexCount; ++i) {
            vertices[i].showEdges();
        }
    }

    Vertex* getVertex(int id) {
        for (int i = 0; i < vertexCount; ++i)
            if (vertices[i].id == id)
                return &vertices[i];
        return nullptr;
    }

    virtual ~Graph() {
        delete[] vertices;
    }
};

class DirectedGraph : public Graph {
public:
    void addEdge(int from, int to, float weight) override {
        Vertex* v = getVertex(from);
        if (!v) {
            addVertex(from);
            v = getVertex(from);
        }
        if (!getVertex(to)) addVertex(to);
        v->addEdge(to, weight);
    }
};

class UndirectedGraph : public Graph {
public:
    void addEdge(int from, int to, float weight) override {
        Vertex* v1 = getVertex(from);
        Vertex* v2 = getVertex(to);
        if (!v1) {
            addVertex(from);
            v1 = getVertex(from);
        }
        if (!v2) {
            addVertex(to);
            v2 = getVertex(to);
        }
        v1->addEdge(to, weight);
        v2->addEdge(from, weight);
    }
};

int main() {
    Graph** graphs = new Graph*[2];
    graphs[0] = new DirectedGraph();
    graphs[1] = new UndirectedGraph();

    int choice;
    do {
        cout << "\n--- Graph Menu ---\n";
        cout << "1. Add Vertex\n2. Add Edge\n3. Remove Vertex\n4. Display Graph\n0. Exit\nChoose: ";
        cin >> choice;
        int gtype, from, to, id;
        float weight;
        switch (choice) {
            case 1:
                cout << "Graph Type (0=Directed, 1=Undirected): "; cin >> gtype;
                cout << "Enter vertex ID: "; cin >> id;
                graphs[gtype]->addVertex(id);
                break;
            case 2:
                cout << "Graph Type (0=Directed, 1=Undirected): "; cin >> gtype;
                cout << "From: "; cin >> from;
                cout << "To: "; cin >> to;
                cout << "Weight: "; cin >> weight;
                graphs[gtype]->addEdge(from, to, weight);
                break;
            case 3:
                cout << "Graph Type (0=Directed, 1=Undirected): "; cin >> gtype;
                cout << "Enter vertex ID to remove: "; cin >> id;
                graphs[gtype]->removeVertex(id);
                break;
            case 4:
                cout << "Graph Type (0=Directed, 1=Undirected): "; cin >> gtype;
                graphs[gtype]->display();
                break;
            case 0:
                cout << "Exiting...\n";
                break;
            default:
                cout << "Invalid option.\n";
        }
    } while (choice != 0);

    delete graphs[0];
    delete graphs[1];
    delete[] graphs;
    return 0;
}

