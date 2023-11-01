#include <iostream>
using namespace std;
#define V 4
#define INF 999

void printMatrix(int matrix[][V]) {
  for (int i = 0; i < V; i++) {
    for (int j = 0; j < V; j++) {
      if (matrix[i][j] == INF)
        printf("%4s", "INF");
      else
        printf("%4d", matrix[i][j]);
    }
    printf("\n");
  }
}

void floydWarshall(int graph[][V]) {
  int matrix[V][V], i, j, k;

  for (i = 0; i < V; i++)
    for (j = 0; j < V; j++)
      matrix[i][j] = graph[i][j];

  for (k = 0; k < V; k++) {
    for (i = 0; i < V; i++) {
      for (j = 0; j < V; j++) {
        if (matrix[i][k] + matrix[k][j] < matrix[i][j])
          matrix[i][j] = matrix[i][k] + matrix[k][j];
      }
    }
  }
  printMatrix(matrix);
}

int main() {
  int graph[V][V] = {{0, 3, INF, 5},
                     {2, 0, INF, 4},
                     {INF, 1, 0, INF},
                     {INF, INF, 2, 0}};
  floydWarshall(graph);
}