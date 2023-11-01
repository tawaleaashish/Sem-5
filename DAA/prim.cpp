#include <iostream>
#include <list>
#include <set>
#include <algorithm>
#include <vector>
using namespace std;

struct edges
{
    char node1;
    char node2;
    int weight;
};

struct graph
{
    char vertex1;
    char vertex2;
};

bool isCycle(graph g[], int V, char a, char b)
{
    list<char> close = {};
    list<char> open = {a};
    while (!open.empty())
    {
        char y = open.front();
        open.pop_front();
        close.push_back(y);
        if (find(close.begin(), close.end(), b) != close.end())
        {
            return true;
        }
        for (int i = 0; i < V; i++)
        {
            if (g[i].vertex1 == y)
            {
                if (find(close.begin(), close.end(), g[i].vertex2) == close.end())
                    open.push_back(g[i].vertex2);
            }
            else if (g[i].vertex2 == y)
            {
                if (find(close.begin(), close.end(), g[i].vertex1) == close.end())
                    open.push_back(g[i].vertex1);
            }
        }
    }
    return false;
}

edges SortEdges(edges nextEdge[], int E)
{
    edges t;
    for (int j = 0; j < E; j++)
    {
        for (int k = 0; k < E - j - 1; k++)
        {
            if (nextEdge[k].weight > nextEdge[k + 1].weight)
            {
                t = nextEdge[k];
                nextEdge[k] = nextEdge[k + 1];
                nextEdge[k + 1] = t;
            }
        }
    }
    return nextEdge[0];
}

int Prim(graph g[], int E, int V, edges e[], int min_weight)
{
    vector<edges> nextEdge;
    set<char> visited = {};
    char x = e[0].node1;
    list<char> queue = {x};
    int count = 0;
    while (visited.size() < V)
    {
        while (!queue.empty())
        {
            char x = queue.front();
            queue.pop_front();
            for (int i = 0; i < E; i++)
            {
                if (e[i].node1 == x || e[i].node2 == x)
                {
                    char neighbor = (e[i].node1 == x) ? e[i].node2 : e[i].node1;
                    if (find(visited.begin(), visited.end(), neighbor) == visited.end())
                    {
                        nextEdge.push_back(e[i]);
                        count++;
                    }
                }
            }
        }
        int count2 = 0;
        edges minEdge = SortEdges(nextEdge.data(), count);
        int i;
        nextEdge.clear();
        count = 0;
        if (!isCycle(g, count2, minEdge.node1, minEdge.node2))
        {
            cout << "  " << minEdge.node1 << "\t  " << minEdge.node2 << "\t  " << minEdge.weight << "\n";
            min_weight += minEdge.weight;
            g[count2].vertex1 = minEdge.node1;
            g[count2].vertex2 = minEdge.node2;
            count2++;
            visited.insert(minEdge.node1);
            visited.insert(minEdge.node2);
            queue.clear();
            queue.assign(visited.begin(), visited.end());
        }
    }
    return min_weight;
}

int main()
{
    int V = 9;
    int E = 13;
    edges e[] = {
        {'A', 'B', 4},
        {'B', 'C', 8},
        {'C', 'D', 7},
        {'D', 'E', 9},
        {'E', 'F', 10},
        {'F', 'G', 2},
        {'G', 'H', 1},
        {'H', 'I', 7},
        {'H', 'A', 8},
        {'B', 'H', 11},
        {'C', 'I', 2},
        {'G', 'I', 6},
        {'C', 'F', 4}};
    // int V = 7;
    // int E = 10;
    // edges e[] = {
    //     {'A', 'B', 6},
    //     {'B', 'C', 11},
    //     {'B', 'D', 5},
    //     {'A', 'G', 15},
    //     {'C', 'G', 25},
    //     {'C', 'D', 17},
    //     {'D', 'E', 22},
    //     {'C', 'F', 9},
    //     {'F', 'G', 12},
    //     {'E', 'F', 10}};
    graph g[13] = {};
    int min_weight = 0;
    cout << "Node 1\tNode 2\tWeight\n";
    min_weight = Prim(g, E, V, e, min_weight);
    cout << "\nMinimum spanning tree weight = " << min_weight << "\n";
    return 0;
}