#include <iostream>
#include <list>
#include <string>
using namespace std;

struct Node
{
    char data;
    int freq;
    Node *left;
    Node *right;
};
list<Node *> N;

bool CompareNodes(const Node *a, const Node *b)
{
    return a->freq < b->freq;
}

void GetValues(Node *root, string str)
{
    if (root == nullptr)
    {
        return;
    }
    if (root->left == nullptr && root->right == nullptr)
    {
        cout << " " << root->data << "\t" << str << "\n";
    }
    GetValues(root->left, str + "0");
    GetValues(root->right, str + "1");
}

void Huffman(int n)
{
    if (n > 1)
    {
        Node *t1 = N.front();
        N.pop_front();
        Node *t2 = N.front();
        N.pop_front();
        Node *newNode = new Node{'\0', t1->freq + t2->freq, t1, t2};
        N.push_back(newNode);
        N.sort(CompareNodes);
        Huffman(n - 1);
    }
}

void NewNodes(char arr[], int freq[], int n)
{
    for (int i = 0; i < n; i++)
    {
        N.push_back(new Node{arr[i], freq[i], nullptr, nullptr});
    }
    N.sort(CompareNodes);
    Huffman(n);
}
int main()
{
    char arr[] = {'a', 'b', 'c', 'd', 'e', 'f'};
    int freq[] = {5, 9, 12, 13, 16, 45};
    int size = sizeof(arr) / sizeof(arr[0]);
    NewNodes(arr, freq, size);

    cout << "char  code-word\n";
    string str = "";
    Node *root = N.front();
    GetValues(root, str);

    for (Node *node : N)
    {
        delete node;
    }
}