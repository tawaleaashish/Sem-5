#include<iostream>
#include<list>
#include<algorithm>
using namespace std;
struct edges{
    char node1;
    char node2;
    int weight;
};
struct graph{
    char vertex1;
    char vertex2;
};
bool isCycle(struct graph g[],int V,char a,char b) 
{
    list<char> visited={};
    list<char> queue={a};
    while(!queue.empty())
    {
        char x=queue.front();
        queue.pop_front();
        visited.push_back(x);
        if((find(visited.begin(),visited.end(),b)!=visited.end()))
        {
            return true;
        }
        for(int i=0;i<V;i++)
        {
            if(g[i].vertex1==x)
            {
                if(find(visited.begin(),visited.end(),g[i].vertex2)==visited.end())
                    queue.push_back(g[i].vertex2);
            }
            else if(g[i].vertex2==x)
            {
                if(find(visited.begin(),visited.end(),g[i].vertex1)==visited.end())
                    queue.push_back(g[i].vertex1);
            }
        }
    }
    return false;
}
int main()
{
    int V=9;
    int E=13;
    struct edges e[]={
        {'A','B',4},
        {'B','C',8},
        {'C','D',7},
        {'D','E',9},
        {'E','F',10},
        {'F','G',2},
        {'G','H',1},
        {'H','I',7},
        {'H','A',8},
        {'B','H',11},
        {'C','I',2},
        {'G','I',6},
        {'C','F',4}
    };
    int count=0;
    struct graph g[13]={};
    struct edges t;
    for(int i=0;i<E;i++)
    {
        for(int j=0;j<E-i-1;j++)
        {
            if(e[j].weight>e[j+1].weight)
            {
                t=e[j];
                e[j]=e[j+1];
                e[j+1]=t;
            }
        }
    }
    cout<<"Node 1\tNode 2\tWeight\n"; 
    int min_weight=0;
    list<char> node={};
    for(int i=0;i<E;i++)
    {
        int flag1=0,flag2=0;
        if(find(node.begin(),node.end(),e[i].node1)!=node.end())
        {
            flag1=1;
        }
        if(find(node.begin(),node.end(),e[i].node2)!=node.end())
        {
            flag2=1;
        }
        if(flag1==0 && flag2==0)
        {
            node.push_back(e[i].node1);
            node.push_back(e[i].node2);
            cout<<"  "<<e[i].node1<<"\t  "<<e[i].node2<<"\t  "<<e[i].weight<<"\n";
            min_weight+=e[i].weight;
            g[count].vertex1=e[i].node1;
            g[count].vertex2=e[i].node2;
            count++;
        }
        else if(flag1==0 && flag2==1)
        {
            node.push_back(e[i].node1);
            cout<<"  "<<e[i].node1<<"\t  "<<e[i].node2<<"\t  "<<e[i].weight<<"\n";
            min_weight+=e[i].weight;
            g[count].vertex1=e[i].node1;
            g[count].vertex2=e[i].node2;
            count++;
        }
        else if(flag1==1 && flag2==0)
        {
            node.push_back(e[i].node2);
            cout<<"  "<<e[i].node1<<"\t  "<<e[i].node2<<"\t  "<<e[i].weight<<"\n";
            min_weight+=e[i].weight; 
            g[count].vertex1=e[i].node1;
            g[count].vertex2=e[i].node2;
            count++;
        }
        else if(flag1==1 && flag2==1)
        {
            if (!isCycle(g,count,e[i].node1,e[i].node2)) 
            {
                cout << "  " << e[i].node1 << "\t  " << e[i].node2 << "\t  " << e[i].weight << "\n";
                min_weight += e[i].weight;
                g[count].vertex1 = e[i].node1;
                g[count].vertex2 = e[i].node2;
                count++;
            }
        }
    }
    cout<<"\nMinimun spanning tree weight = "<<min_weight<<"\n";
}