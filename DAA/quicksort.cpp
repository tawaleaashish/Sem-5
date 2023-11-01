#include<iostream>
using namespace std;

void printarray(int a[],int n)
{
    for(int i=0;i<n;i++)
    {
        cout<<a[i]<<" ";
    }
}
int divide(int a[],int low,int high)
{
    int i=low-1,t;
    for(int j=low;j<high;j++)
    {
        if(a[j]<=a[high])
        {
            i++;
            t=a[j];
            a[j]=a[i];
            a[i]=t;
        }
    }
    t=a[i+1];
    a[i+1]=a[high];
    a[high]=t;
    return (i+1);
}
void quicksort(int a[],int low,int high)
{
    if(low<high)
    {
        int pos=divide(a,low,high);
        quicksort(a,low,pos-1);
        quicksort(a,pos+1,high);
    }
}
int main()
{
    int n;
    cout<<"Enter number of elements: ";
    cin>>n;
    int i=0,a[n],x[n]={};
    while(i<n)
    {
        cout<<"Element "<<i+1<<": ";
        cin>>a[i];
        i++;
    }
    quicksort(a,0,n-1);
    printarray(a,n);
}